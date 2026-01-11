from pgzero.actor import Actor


class Character:
    def __init__(self, image_direction, init_pos):
        self.actor = Actor(image_direction)
        self.init_pos = init_pos
        self.frame_index = 0
        self.vx = 0
        self.vy = 0

        self.actor.pos = self.init_pos
