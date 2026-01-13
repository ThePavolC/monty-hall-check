import logging
import random

ITERATIONS = 100000
FORCE_SWITCH = True
LOG_LEVEL = logging.INFO

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())
log.setLevel(LOG_LEVEL)


class Goat:
    def __str__(self) -> str:
        return "Goat"


class Car:
    def __str__(self) -> str:
        return "Car"


def set_doors() -> list:
    """Set up the doors with two goats and one car, then shuffle them."""
    doors = [Goat(), Goat(), Car()]
    random.shuffle(doors)
    return doors


def find_goat(doors: list, user_pick: int) -> int:
    """Finds a door position with a goat that is not the user's pick."""
    goat_positions = []
    for i, door in enumerate(doors):
        if i != user_pick and isinstance(door, Goat):
            goat_positions.append(i)
    return random.choice(goat_positions)


def is_winner(doors: list, pick: int) -> bool:
    """Check if the picked door has a car behind it."""
    return isinstance(doors[pick], Car)


def switch_choice(current_pick: int, host_position: int) -> int:
    """Get the position of the door to switch to."""
    return next(i for i in range(3) if i != current_pick and i != host_position)


def closed_doors(doors: list, host_position: int) -> list:
    """Get a list of door positions excluding the host's position."""
    return [i for i, _ in enumerate(doors) if i != host_position]


def monty_hall_run(
    doors: list, host_position: int, user_position: int, force_switch: bool
) -> bool:
    """Simulate a single Monty Hall game run."""
    should_switch = force_switch or random.choice([True, False])
    if should_switch:
        user_position = switch_choice(user_position, host_position)
        log.debug(f"MontyHall: User switched to: {user_position}")

    is_win = is_winner(doors, user_position)
    log.debug(
        f"MontyHall: User pick: {user_position} and {'WON' if is_win else 'LOST'}"
    )

    return is_win


def one_of_two_run(doors: list, host_position: int) -> bool:
    """Simulate a single One of Two game run, where
    user picks randomly one of the two remaining doors.
    """
    possible_doors_to_open = closed_doors(doors, host_position)
    one_of_two_choice = random.choice(possible_doors_to_open)

    is_win = is_winner(doors, one_of_two_choice)
    log.debug(
        f"OneOfTwo: User pick: {one_of_two_choice} and {'WON' if is_win else 'LOST'}"
    )
    return is_win


def run(iterations: int, force_switch: bool = False):
    """Runs the simulations for a given number of iterations."""
    # counts monty hall runs with switching and without switching
    monty_hall_runs = []
    # counts runs where picks random one of two options left
    one_of_two_runs = []

    for idx in range(iterations):
        log.debug(f"--- Iteration {idx+1} ---")

        doors = set_doors()
        user_pick = random.randint(0, 2)
        host_position = find_goat(doors, user_pick)

        log.debug(f"Doors: {[str(door) for door in doors]}")
        log.debug(f"User pick: {user_pick}")
        log.debug(f"Host position: {host_position}")
        log.debug('----------------')

        one_of_two_runs.append(one_of_two_run(doors, host_position))
        monty_hall_runs.append(
            monty_hall_run(doors, host_position, user_pick, force_switch)
        )

    log.debug('--- Summary ---')

    wins = sum(monty_hall_runs)
    log.info(
        f"MontyHall: Total wins: {wins} out of {iterations} with probability {wins/iterations:.2f}"
    )

    wins = sum(one_of_two_runs)
    log.info(
        f"OneOfTwo: Total wins: {wins} out of {iterations} with probability {wins/iterations:.2f}"
    )


if __name__ == "__main__":
    run(ITERATIONS, FORCE_SWITCH)
