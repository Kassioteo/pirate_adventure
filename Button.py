from pgzero.actor import Actor


class Button:
    def __init__(self, image_direction, pos):
        self.actor = Actor(image_direction, pos)


play_button = Button("play_button", (450, 400))
exit_butoon = Button("exit_button", (940, 20))
music_button = Button("exit_button", (40, 20))
exit_game_button = Button("play_button", (450, 450))
return_button = Button("play_button", (450, 350))
