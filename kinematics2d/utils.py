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
    if epsilon is None:
        epsilon = EPSILON
    return abs(a - b) <= epsilon


def rad_from_deg(value: float) -> float:
    return np.deg2rad(value)


def deg_from_rad(value: float) -> float:
    return np.rad2deg(value)


def angle_cap(value: float) -> float:
    """Convert an angle to be between -PI and PI."""
    capped_value = value % (2.0 * PI)
    return capped_value if capped_value <= PI else capped_value - 2.0 * PI


def angle_diff(origin: float, taget: float) -> float:
    """Calculate the smallest difference between origin from target."""
    return angle_cap(angle_cap(origin) - angle_cap(taget))
