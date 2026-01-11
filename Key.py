from Character import Character
from utils import set_animation_list


class Key(Character):
    def __init__(self):
        super().__init__("key_0", (64 * 15 - 150, 64 * 10 - 190))
        idle_animation = set_animation_list("key", 8)
        self.idle_animation = idle_animation

    def animete_key_idle(self):
        self.frame_index = (self.frame_index + 1) % len(self.idle_animation)
        self.actor.image = self.idle_animation[self.frame_index]
