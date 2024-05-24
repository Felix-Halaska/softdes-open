"""
Calculate the terminal velocity of a sphere falling with drag.
"""


def terminal_velocity(mass, cross_sectional_area, timestep):
    """
    Calculate the terminal velocity of a sphere with a given mass and
    cross-sectional area.

    Given the mass and cross-sectional area of a sphere, use Euler's method
    with the given timestep to calculate the terminal velocity of the falling
    sphere. Positive velocity is considered upward, so the terminal velocity
    will always be negative.

    To avoid issues in simulation, the value of dt is expected to be relatively
    small.

    Args:
        m: An int or float representing the mass of the sphere in kg.
        A: An int or float representing the cross-sectional area of the sphere
            in m^2.
        dt: An int or float representing the timestep for Euler's method, in
            seconds.

    Returns:
        A float representing the terminal velocity of the sphere.
    """
    acceleration_threshold = 0.0001
    gravity = -9.8
    rho = 1
    drag_coefficient = 0.5
    previous_velocity = 0
    current_velocity = 0
    force_of_gravity = mass * gravity
    while (
        previous_velocity == 0
        or abs(current_velocity - previous_velocity) > acceleration_threshold
    ):
        previous_velocity = current_velocity
        force_of_drag = (
            0.5
            * rho
            * drag_coefficient
            * cross_sectional_area
            * current_velocity**2
        )
        delta_velocity = ((force_of_gravity + force_of_drag) * timestep) / mass
        current_velocity = current_velocity + delta_velocity
    return current_velocity
