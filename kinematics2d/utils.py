import numpy as np

__all__ = ["pi", "rad_from_deg", "deg_from_rad", "angle_cap", "angle_diff"]


pi = np.pi


def rad_from_deg(value: float) -> float:
    return np.deg2rad(value)


def deg_from_rad(value: float) -> float:
    return np.rad2deg(value)


def angle_cap(value: float) -> float:
    capped_value = value % (2.0 * pi)
    return capped_value if capped_value <= pi else capped_value - 2.0 * pi


def angle_diff(origin: float, taget: float) -> float:
    return angle_cap(angle_cap(origin) - angle_cap(taget))
