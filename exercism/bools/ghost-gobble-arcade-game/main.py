def eat_ghost(has_a_power_pellet_active: bool,
              is_touching_a_ghost: bool) -> bool:
    return has_a_power_pellet_active and is_touching_a_ghost


def score(is_touching_a_power_pellet: bool, is_touching_a_dot: bool) -> bool:
    return is_touching_a_power_pellet or is_touching_a_dot


def lose(has_a_power_pellet_active: bool, is_touching_a_ghost: bool) -> bool:
    return is_touching_a_ghost and not has_a_power_pellet_active


def win(has_eaten_all_dots: bool, has_a_power_pellet_active: bool,
        is_touching_a_ghost: bool) -> bool:

    return has_eaten_all_dots and not \
        lose(has_a_power_pellet_active, is_touching_a_ghost)
