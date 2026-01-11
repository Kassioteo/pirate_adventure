from Game import Game
from Pirate import Pirate
from Character import Character
from Key import Key
from Platform import Platform, Cannon_fire
from Enemie import Shell, Crabby, Ball
from utils import start_all_clock, stop_all_clocks
from Button import (
    play_button,
    music_button,
    exit_game_button,
    exit_butoon,
    return_button,
)

music.play("trilha_sonora.wav")

engine = Game()
# CONSTANTS
WIDTH = engine.width
HEIGHT = engine.height
TITLE = engine.title

# CREATING

# Pirate
pirate = Pirate()

# chest
chest = Character("chest_idle", (WIDTH - 900, HEIGHT - 420))

# key
key = Key()

# enemies list

shell = Shell(pirate.actor)
crabby = Crabby()
ball = Ball()

enimie_list = [shell, crabby, ball]

# platforms list

platform_0 = Platform("platform_0", (WIDTH - 720, HEIGHT - 20))
platform_1 = Platform("platform_0", (WIDTH - 720, HEIGHT - 380))

platform_2 = Platform("platform_1", (WIDTH - 400, HEIGHT - 90))
platform_3 = Platform("platform_1", (WIDTH - 380, HEIGHT - 290))

platform_4 = Platform("platform_2", (WIDTH - 160, HEIGHT - 90))

cannon_fire = Cannon_fire()

platforms_list = [
    platform_0,
    platform_1,
    platform_2,
    platform_3,
    platform_4,
    cannon_fire,
]


def on_mouse_down(pos):
    if engine.game_state == "MENU":
        if play_button.actor.collidepoint(pos):
            stop_all_clocks(
                pirate.animete_pirate_idle,
                pirate.animete_pirate_run,
                shell.animete_shell_attack,
                crabby.animete_crabby_run,
                cannon_fire.fire_cannon,
                key.animete_key_idle,
            )
            engine.action_play_button(pirate.actor)
            start_all_clock(
                pirate.animete_pirate_idle,
                pirate.animete_pirate_run,
                shell.animete_shell_attack,
                crabby.animete_crabby_run,
                cannon_fire.fire_cannon,
                key.animete_key_idle,
            )
        elif music_button.actor.collidepoint(pos):
            engine.action_music_button(music)
        elif exit_game_button.actor.collidepoint(pos):
            engine.action_exit_game_button()

    elif engine.game_state == "GAME":
        if exit_butoon.actor.collidepoint(pos):
            engine.action_exit_button()

    elif engine.game_state == "END":
        if return_button.actor.collidepoint(pos):
            engine.action_return_button()


def draw():
    if engine.game_state == "MENU":
        screen.fill((30, 30, 30))
        screen.draw.text(
            "Pirate Adventure", center=(450, 150), fontsize=60, color="white"
        )
        play_button.actor.draw()
        exit_game_button.actor.draw()
        music_button.actor.draw()

    elif engine.game_state == "GAME":
        screen.clear()
        screen.fill("skyblue")

        exit_butoon.actor.draw()

        pirate.actor.draw()

        if not pirate.have_key:
            key.actor.draw()

        chest.actor.draw()

        for enemie in enimie_list:
            enemie.actor.draw()

        for platform in platforms_list:
            platform.actor.draw()

    elif engine.game_state == "END":
        screen.fill((30, 30, 30))
        screen.draw.text(
            "PARABENS VC GANHOU!!!", center=(450, 150), fontsize=60, color="white"
        )
        return_button.actor.draw()


def update():

    # ENEMY MOVEMENT

    # Crabby
    crabby.crabby_walk()

    # Ball
    ball.ball_walk(cannon_fire.frame_index, cannon_fire.animation)

    # vertical physics
    platform_under, platform_over = pirate.start_physic_vertical_pirate_y(
        platforms_list
    )

    # horizontal physics
    platform_left, platform_right = pirate.start_physic_horizontal_pirate_x(
        platforms_list
    )

    # collision with enemies
    pirate.collision_enemies(enimie_list)

    #  collision with key
    pirate.collision_key(key.actor)

    #  collision with chest
    if pirate.collision_chest(chest.actor) == "END":
        engine.game_state = pirate.collision_chest(chest.actor)
