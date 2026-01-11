from Character import Character
from utils import set_animation_list
from pgzero.keyboard import keyboard


class Pirate(Character):
    def __init__(self):
        super().__init__("pirate_idle_0", (5, 540))

        idle_animation = set_animation_list("pirate_idle", 5)
        run_left_animation = set_animation_list("pirate_run_left", 5)
        run_right_animation = set_animation_list("pirate_run_right", 5)

        self.idle_animation = idle_animation
        self.run_left_animation = run_left_animation
        self.run_right_animation = run_right_animation

        self.run_frame = 0

        self.have_key = False

    def animete_pirate_idle(self):
        if self.vx == 0 and self.vy == 0:
            self.frame_index = (self.frame_index + 1) % len(self.idle_animation)
            self.actor.image = self.idle_animation[self.frame_index]

    def animete_pirate_run(self):
        if self.vy == 0 and self.vx > 0:
            self.run_frame = (self.run_frame + 1) % len(self.run_right_animation)
            self.actor.image = self.run_right_animation[self.run_frame]
        elif self.vy == 0 and self.vx < 0:
            self.run_frame = (self.run_frame + 1) % len(self.run_left_animation)
            self.actor.image = self.run_left_animation[self.run_frame]

    def horizontal_collision_x(self, list_platforms):
        platform_left = False
        platform_right = False

        for platform in list_platforms:

            if self.actor.colliderect(platform.actor):

                if self.vx < 0:
                    self.actor.left = platform.actor.right
                    platform_left = True
                elif self.vx > 0:
                    self.actor.right = platform.actor.left
                    platform_right = True
        return platform_left, platform_right

    def vertical_collision_y(self, list_platforms):
        platform_under = False
        platform_over = False

        for platform in list_platforms:

            if self.actor.colliderect(platform.actor):

                if self.vy > 0:
                    self.actor.bottom = platform.actor.top
                    self.vy = 0
                    platform_under = True
                elif self.vy < 0:
                    self.actor.top = platform.actor.bottom
                    self.vy = 0
                    platform_over = True
        return platform_under, platform_over

    def start_physic_vertical_pirate_y(self, list_platforms):
        self.vy = self.vy + 0.5
        self.actor.y = self.actor.y + self.vy

        if self.actor.y > 64 * 10:
            self.actor.pos = self.init_pos

        platform_under, platform_over = self.vertical_collision_y(list_platforms)

        if keyboard.space:
            if platform_under:
                self.vy = -13

        return platform_under, platform_over

    def start_physic_horizontal_pirate_x(self, list_platforms):
        self.vx = 0

        if keyboard.left:
            self.vx = -5
        if keyboard.right:
            self.vx = 5

        self.actor.x = self.actor.x + self.vx

        if self.actor.left < 0:
            self.actor.left = 0
        if self.actor.right > 64 * 15:
            self.actor.right = 64 * 15

        platform_left, platform_right = self.horizontal_collision_x(list_platforms)

        return platform_left, platform_right

    def collision_enemies(self, list_enemies):
        for enemy in list_enemies:
            if self.actor.colliderect(enemy.actor):
                self.actor.pos = self.init_pos
                self.have_key = False
                break

    def collision_key(self, key_actor):
        if self.actor.colliderect(key_actor):
            self.have_key = True

    def collision_chest(self, chest_actor):
        if self.actor.colliderect(chest_actor):
            if self.have_key:
                return "END"
            else:
                return None

    def reset_pos(self):
        self.actor.pos = self.init_pos
