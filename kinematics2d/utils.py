"""Utility functions."""

import numpy as np

__all__ = ["pi", "rad_from_deg", "deg_from_rad"]


pi = np.pi


def rad_from_deg(value: float) -> float:
    return np.deg2rad(value)


def deg_from_rad(value: float) -> float:
    return np.rad2deg(value)
