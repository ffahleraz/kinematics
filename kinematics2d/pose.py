import math
from typing import Optional

import numpy as np

import kinematics2d as km

__all__ = ["Pose"]


class Pose:
    """A 2-dimensional pose.

    Attributes:
        - position: km.Vector
        - orientation: float (in radians)
    """

    def __init__(self, position: km.Vector, orientation: float) -> None:
        self._position: km.Vector = position
        self._orientation: float = orientation

    @classmethod
    def from_copy(cls, source: "Pose") -> "Pose":
        return cls(km.Vector.from_copy(source.position), source.orientation)

    @classmethod
    def zeros(cls) -> "Pose":
        return cls(km.Vector.zeros(), 0.0)

    @property
    def position(self) -> km.Vector:
        return self._position

    @position.setter
    def position(self, value: km.Vector) -> None:
        self._position = value

    @property
    def orientation(self) -> float:
        return self._orientation

    @orientation.setter
    def orientation(self, value: float) -> None:
        self._orientation = value

    def __repr__(self) -> str:
        return "Pose(pos: {}, ort: {})".format(self._position, self._orientation)

    def __add__(self, other: "Pose") -> "Pose":
        """Calculate the transformation of other to the coordinate frame of self."""
        return Pose(
            self._position + other.position.rotated(self._orientation),
            self._orientation + other.orientation,
        )

    def __sub__(self, other: "Pose") -> "Pose":
        """Calculate the transformation of self to the coordinate frame of other."""
        return Pose(
            (self._position - other.position).rotated(-other.orientation),
            self._orientation - other.orientation,
        )

    def is_at_position(
        self, target: km.Vector, tolerance: Optional[float] = 0.0
    ) -> bool:
        return math.abs(target - self._position) <= tolerance

    def is_at_orientation(
        self, target: float, tolerance: Optional[float] = 0.0
    ) -> bool:
        return math.abs(km.angle_diff(self._orientation, target)) <= tolerance

    def is_at(
        self,
        target: "Pose",
        pos_tolerance: Optional[float] = 0.0,
        ort_tolerance: Optional[float] = 0.0,
    ) -> bool:
        return self.is_at_position(
            target.position, pos_tolerance
        ) and self.is_at_orientation(target.orientation, ort_tolerance)
