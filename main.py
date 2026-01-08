WIDTH = 64 * 15
HEIGHT = 64 * 10
TITLE = "Pirate Adventure"

# criando o Pirata
pirate = Actor("pirate_idle_0", (500, 500))
pirate.pos = 5, HEIGHT / 2
pirate.vy = 0
pirate.vx = 0


# criando plataformas
plataforma_0 = Actor("plataforma_0")
plataforma_0.pos = 50, HEIGHT

plataforma_1 = Actor("plataforma_0")
plataforma_1.pos = 145, HEIGHT

plataforma_2 = Actor("plataforma_0")
plataforma_2.pos = 240, HEIGHT

plataforma_3 = Actor("plataforma_0")
plataforma_3.pos = 335, HEIGHT

plataforma_4 = Actor("plataforma_0")
plataforma_4.pos = 430, HEIGHT

plataforma_5 = Actor("plataforma_0")
plataforma_5.pos = 525, HEIGHT

plataforma_6 = Actor("plataforma_2")
plataforma_6.pos = 640, 560

plataforma_7 = Actor("plataforma_1")
plataforma_7.pos = 770, 490

plataforma_8 = Actor("plataforma_1")
plataforma_8.pos = 930, 390


# funcao criadora de lista de sprites
def set_animation_list(animation_name, list_size):
    image_list = []

    for i in range(0, list_size):
        image_list.append(f"{animation_name}_{i}")

    return image_list


# listas de sprites
pirate_idle = set_animation_list("pirate_idle", 5)
pirate_run_left = set_animation_list("pirate_run_left", 5)
pirate_run_right = set_animation_list("pirate_run_right", 5)

# animacoes

# pirata


# idle
pirate_idle_frame = 0


def animete_pirate_idle():
    global pirate_idle_frame

    if pirate.vx == 0 and pirate.vy == 0:
        pirate_idle_frame = (pirate_idle_frame + 1) % len(pirate_idle)

        pirate.image = pirate_idle[pirate_idle_frame]


clock.schedule_interval(animete_pirate_idle, 0.1)

# run
pirate_run_frame = 0


def animete_pirate_run():
    global pirate_run_frame
    if pirate.vy == 0 and pirate.vx > 0:
        pirate_run_frame = (pirate_run_frame + 1) % len(pirate_run_right)
        pirate.image = pirate_run_right[pirate_run_frame]
    elif pirate.vy == 0 and pirate.vx < 0:
        pirate_run_frame = (pirate_run_frame + 1) % len(pirate_run_left)
        pirate.image = pirate_run_left[pirate_run_frame]


clock.schedule_interval(animete_pirate_run, 0.1)


def draw():
    screen.clear()
    screen.fill('skyblue')
    plataforma_0.draw()
    plataforma_1.draw()
    plataforma_2.draw()
    plataforma_3.draw()
    plataforma_4.draw()
    plataforma_5.draw()
    plataforma_6.draw()
    plataforma_7.draw()
    plataforma_8.draw()
    pirate.draw()


def update():
    # dando movimento horizontal
    pirate.vx = 0

    if keyboard.left:
        pirate.vx = -5
    if keyboard.right:
        pirate.vx = 5

    pirate.x = pirate.x + pirate.vx

    if pirate.left < 0:
        pirate.left = 0

    if pirate.right > WIDTH:
        pirate.right = WIDTH
