from pgzero.clock import clock


def set_animation_list(animation_name, list_size):
    image_list = []

    for i in range(0, list_size):
        image_list.append(f"{animation_name}_{i}")

    return image_list


def start_all_clock(
    animete_pirate_idle,
    animete_pirate_run,
    animete_shell_attack,
    animete_crabby_run,
    animete_cannon_fire,
    animete_key,
):
    clock.schedule_interval(animete_pirate_idle, 0.1)
    clock.schedule_interval(animete_pirate_run, 0.1)
    clock.schedule_interval(animete_shell_attack, 0.1)
    clock.schedule_interval(animete_crabby_run, 0.1)
    clock.schedule_interval(animete_cannon_fire, 4.0)
    clock.schedule_interval(animete_key, 0.1)


def stop_all_clocks(
    animete_pirate_idle,
    animete_pirate_run,
    animete_shell_attack,
    animete_crabby_run,
    animete_cannon_fire,
    animete_key,
):
    clock.unschedule(animete_pirate_idle)
    clock.unschedule(animete_pirate_run)
    clock.unschedule(animete_shell_attack)
    clock.unschedule(animete_crabby_run)
    clock.unschedule(animete_cannon_fire)
    clock.unschedule(animete_key)
