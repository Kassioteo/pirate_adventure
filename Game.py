import sys
from pgzero.actor import Actor


class Game:
    def __init__(self):
        self.width = 64 * 15
        self.height = 64 * 10
        self.title = "Pirate Adventure"
        self.game_state = "MENU"
        self.music_state = True

    # on_mouse_dowm
    def action_play_button(self, pirate_actor):
        pirate_actor.have_key = False
        self.game_state = "GAME"

    def action_music_button(self, music):
        if self.music_state:
            self.music_state = False
            music.pause()
        else:
            self.music_state = True
            music.unpause()

    def action_exit_game_button(self):
        sys.exit()

    def action_exit_button(self):
        self.game_state = "MENU"

    def action_return_button(self):
        self.game_state = "MENU"
