import typing

import numpy as np

__all__ = [
    "PI",
    "EPSILON",
    "is_close",
    "rad_from_deg",
    "deg_from_rad",
    "angle_cap",
    "angle_diff",
]


PI = np.pi
EPSILON = 1e-9


def is_close(a: float, b: float, epsilon: typing.Optional[float] = None) -> bool:
    """Check if the difference between two floats is less than or equal to epsilon."""
    if epsilon is None:
        epsilon = EPSILON
    return abs(a - b) <= epsilon


def rad_from_deg(value: float) -> float:
    return np.deg2rad(value)


def deg_from_rad(value: float) -> float:
    return np.rad2deg(value)


def angle_cap(value: float) -> float:
    """Convert an angle (in radian) to be between -PI and PI."""
    capped_value = value % (2.0 * PI)
    return capped_value if capped_value <= PI else capped_value - 2.0 * PI


def angle_diff(target: float, origin: float) -> float:
    """Calculate the smallest difference (in radian) between target from origin."""
    return angle_cap(angle_cap(target) - angle_cap(origin))
