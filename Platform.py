from utils import set_animation_list
from pgzero.actor import Actor
from pgzero.clock import clock


class Platform:
    def __init__(self, image_direction, pos):
        self.actor = Actor(image_direction)
        self.actor.pos = pos


class Cannon_fire(Platform):
    def __init__(self):
        super().__init__("cannon_fire_idle", (64 * 15 - 210, 64 * 10 - 172))
        self.frame_index = 0
        animation = set_animation_list("cannon_fire", 6)
        self.animation = animation

    def animete_cannon_fire(self):
        self.frame_index = (self.frame_index + 1) % len(self.animation)
        self.actor.image = self.animation[self.frame_index]

        if self.frame_index == len(self.animation) - 1:
            clock.unschedule(self.animete_cannon_fire)
            self.frame_index = 0
        # self.frame_index += 1

        # if self.frame_index < len(self.animation):
        #     self.actor.image = self.animation[self.frame_index]
        # else:
        #     clock.unschedule(self.animete_cannon_fire)
        #     self.frame_index = 0
        #     self.actor.image = "cannon_fire_idle"

    def fire_cannon(self):
        clock.schedule_interval(self.animete_cannon_fire, 0.1)
        # self.frame_index = 0
        # clock.unschedule(self.animete_cannon_fire)
        # clock.schedule_interval(self.animete_cannon_fire, 0.1)
