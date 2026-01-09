# horizontal
WIDTH = 64 * 15
# vertical
HEIGHT = 64 * 10
TITLE = "Pirate Adventure"
POSICAO_INICIAL = 5, HEIGHT - 100

# criando o Pirata
pirate = Actor("pirate_idle_0")
pirate.pos = POSICAO_INICIAL
pirate.vy = 0
pirate.vx = 0


# criando inimigos
list_inimigos = []

# inimigo 0
shell_0 = Actor("shell_idle")
shell_0.pos = WIDTH - 720, HEIGHT - 60
shell_0.vy = 0
shell_0.vx = 0
list_inimigos.append(shell_0)

# inimigo 1
crabby_0 = Actor("crabby_run_0")
crabby_0.pos = WIDTH - 720, HEIGHT - 410
crabby_0.vy = 0
crabby_0.vx = 3
list_inimigos.append(crabby_0)

# inimigo 2
ball_0 = Actor("ball_idle")
ball_0.pos = WIDTH - 200, HEIGHT - 190
ball_0.vy = 0
ball_0.vx = 3
list_inimigos.append(ball_0)

# criando plataformas
list_plataforma = []

plataforma_00 = Actor("plataforma_0")
plataforma_00.pos = WIDTH - 720, HEIGHT - 20
list_plataforma.append(plataforma_00)


plataforma_01 = Actor("plataforma_0")
plataforma_01.pos = WIDTH - 720, HEIGHT - 380
list_plataforma.append(plataforma_01)


plataforma_20 = Actor("plataforma_2")
plataforma_20.pos = WIDTH - 400, HEIGHT - 90
list_plataforma.append(plataforma_20)


plataforma_21 = Actor("plataforma_2")
plataforma_21.pos = WIDTH - 380, HEIGHT - 290
list_plataforma.append(plataforma_21)


plataforma_10 = Actor("plataforma_1")
plataforma_10.pos = WIDTH - 160, HEIGHT - 90
list_plataforma.append(plataforma_10)

cannon_fire_0 = Actor("cannon_fire_idle")
cannon_fire_0.pos = WIDTH - 200, HEIGHT - 190
list_plataforma.append(cannon_fire_0)

# criando funcao de colisao colisao


def colisao_plataforma_x():
    platform_left = False
    platform_right = False

    for plataforma in list_plataforma:

        if pirate.colliderect(plataforma):

            if pirate.vx < 0:
                pirate.left = plataforma.right
                platform_left = True
            elif pirate.vx > 0:
                pirate.right = plataforma.left
                platform_right = True
    return platform_left, platform_right


def colisao_plataforma_y():
    platform_under = False
    platform_over = False

    for plataforma in list_plataforma:

        if pirate.colliderect(plataforma):

            if pirate.vy > 0:
                pirate.bottom = plataforma.top
                pirate.vy = 0
                platform_under = True
            elif pirate.vy < 0:
                pirate.top = plataforma.bottom
                pirate.vy = 0
                platform_over = True
    return platform_under, platform_over


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
shell_atack = set_animation_list("shell_atack", 6)
crabby_run = set_animation_list("crabby_run", 6)
cannon_fire = set_animation_list("cannon_fire", 6)

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


# inimigos

# shell_atack
shell_atack_frame = 0


def animete_shell_atack():
    global shell_atack_frame
    shell_0.image = "shell_idle"
    distance = pirate.distance_to(shell_0)
    if distance < 120:
        shell_atack_frame = (shell_atack_frame + 1) % len(shell_atack)
        shell_0.image = shell_atack[shell_atack_frame]


clock.schedule_interval(animete_shell_atack, 0.1)

# crabby
crabby_run_frame = 0


def animete_crabby_run():
    global crabby_run_frame
    crabby_run_frame = (crabby_run_frame + 1) % len(crabby_run)
    crabby_0.image = crabby_run[crabby_run_frame]


clock.schedule_interval(animete_crabby_run, 0.1)


# cannon_fire
cannon_fire_frame = 0
fire = True


def animete_cannon_fire():
    global cannon_fire_frame

    cannon_fire_frame = (cannon_fire_frame + 1) % len(cannon_fire)
    cannon_fire_0.image = cannon_fire[cannon_fire_frame]

    # if cannon_fire_frame == len(cannon_fire) - 2:
    #     ball_0.pos = WIDTH - 200, HEIGHT - 190

    if cannon_fire_frame == len(cannon_fire) - 1:
        clock.unschedule(animete_cannon_fire)
        cannon_fire_frame = 0


def fire_cannon_fire():
    clock.schedule_interval(animete_cannon_fire, 0.1)


clock.schedule_interval(fire_cannon_fire, 5.0)


# movimentacao de inimigos


# crabby
def crabby_walk():
    crabby_0.x = crabby_0.x - crabby_0.vx
    if crabby_0.left < 10 or crabby_0.right > 470:
        crabby_0.vx = -crabby_0.vx


# ball
def ball_walk():
    global cannon_fire_frame
    ball_0.x = ball_0.x - ball_0.vx

    if cannon_fire_frame == len(cannon_fire) - 3:
        ball_0.pos = WIDTH - 200, HEIGHT - 190


def draw():
    screen.clear()
    screen.fill("skyblue")
    plataforma_00.draw()
    plataforma_01.draw()
    plataforma_20.draw()
    plataforma_21.draw()
    plataforma_10.draw()
    pirate.draw()
    shell_0.draw()
    crabby_0.draw()
    ball_0.draw()
    cannon_fire_0.draw()


def update():

    crabby_walk()
    ball_walk()
    # vertical ----------

    # gravidade
    pirate.vy = pirate.vy + 0.5
    pirate.y = pirate.y + pirate.vy

    # queda
    if pirate.y > HEIGHT:
        pirate.pos = 5, HEIGHT - 100

    # colisao vertical
    platform_under, platform_over = colisao_plataforma_y()

    # dando movimento vertical
    if keyboard.space:
        if platform_under:
            pirate.vy = -12

    # horizontal --------------

    # dando movimento horizontal
    pirate.vx = 0

    if keyboard.left:
        pirate.vx = -5
    if keyboard.right:
        pirate.vx = 5

    pirate.x = pirate.x + pirate.vx

    # colisao horizontal
    platform_left, platform_right = colisao_plataforma_x()

    # colisao inimigos
    for enemy in list_inimigos:
        if pirate.colliderect(enemy):
            pirate.pos = POSICAO_INICIAL
            break

    # colisao fim do mapa horizontal
    if pirate.left < 0:
        pirate.left = 0
    if pirate.right > WIDTH:
        pirate.right = WIDTH
