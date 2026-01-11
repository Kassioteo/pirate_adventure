from pgzero.actor import Actor
from utils import set_animation_list


class Enemie:
    def __init__(self, idle_direction, animation_direction, len_anim, init_pos, vy, vx):
        self.actor = Actor(idle_direction)
        self.actor.pos = init_pos
        animation = set_animation_list(animation_direction, len_anim)
        self.animation = animation
        self.frame_index = 0
        self.vy = vy
        self.vx = vx


class Shell(Enemie):
    def __init__(self, pirate_actor):
        super().__init__(
            "shell_idle", "shell_attack", 6, (64 * 15 - 720, 64 * 10 - 60), 0, 0
        )
        self.pirate_actor = pirate_actor

    def animete_shell_attack(self):
        self.actor.image = "shell_idle"
        distance = self.pirate_actor.distance_to(self.actor)
        if distance < 120:
            self.frame_index = (self.frame_index + 1) % len(self.animation)
            self.actor.image = self.animation[self.frame_index]


class Crabby(Enemie):
    def __init__(self):
        super().__init__(
            "crabby_run_0", "crabby_run", 6, (64 * 15 - 740, 64 * 10 - 420), 0, 3
        )

    def animete_crabby_run(self):
        self.frame_index = (self.frame_index + 1) % len(self.animation)
        self.actor.image = self.animation[self.frame_index]

    def crabby_walk(self):
        self.actor.x = self.actor.x - self.vx
        if self.actor.left < 10 or self.actor.right > 470:
            self.vx = -self.vx


class Ball(Enemie):
    def __init__(self):
        super().__init__("ball_idle", "", 0, (64 * 15 - 225, 64 * 10 - 172), 0, 3)

    def ball_walk(self, cannon_frame_index, cannon_animation):
        self.actor.x = self.actor.x - self.vx
        if cannon_frame_index == len(cannon_animation) - 3:
            self.actor.pos = 64 * 15 - 225, 64 * 10 - 172
