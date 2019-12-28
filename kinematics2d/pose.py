import math
import typing

import kinematics2d as k2d

__all__ = ["Pose"]


class Pose:
    """A 2-dimensional pose.

    Attributes:
        - position: k2d.Vector
        - orientation: float (in radians)
    """

    def __init__(self, position: k2d.Vector, orientation: float) -> None:
        self._position: k2d.Vector = k2d.Vector.from_copy(position)
        self._orientation: float = orientation

    @classmethod
    def from_copy(cls, source: "Pose") -> "Pose":
        return cls(k2d.Vector.from_copy(source.position), source.orientation)

    @classmethod
    def zeros(cls) -> "Pose":
        return cls(k2d.Vector.zeros(), 0.0)

    @property
    def position(self) -> k2d.Vector:
        return self._position

    @position.setter
    def position(self, value: k2d.Vector) -> None:
        self._position.x = value.x
        self._position.y = value.y

    @property
    def orientation(self) -> float:
        return self._orientation

    @orientation.setter
    def orientation(self, value: float) -> None:
        self._orientation = value

    def __repr__(self) -> str:
        return "Pose(pos: {}, ort: {})".format(self.position, self.orientation)

    def __add__(self, other: "Pose") -> "Pose":
        """Calculate the transformation of other to the coordinate frame of self."""
        return Pose(
            self.position + other.position.rotated(self.orientation),
            self.orientation + other.orientation,
        )

    def __iadd__(self, other: "Pose") -> "Pose":
        return self + other

    def __sub__(self, other: "Pose") -> "Pose":
        """Calculate the transformation of self to the coordinate frame of other."""
        return Pose(
            (self.position - other.position).rotated(-other.orientation),
            self.orientation - other.orientation,
        )

    def __isub__(self, other: "Pose") -> "Pose":
        return self - other

    def is_at_position(
        self, target: k2d.Vector, tolerance: typing.Optional[float] = None
    ) -> bool:
        if tolerance is None:
            tolerance = k2d.EPSILON
        return abs(target - self.position) <= tolerance

    def is_at_orientation(
        self, target: float, tolerance: typing.Optional[float] = None
    ) -> bool:
        if tolerance is None:
            tolerance = k2d.EPSILON
        return abs(k2d.angle_diff(self.orientation, target)) <= tolerance

    def is_at(
        self,
        target: "Pose",
        pos_tolerance: typing.Optional[float] = None,
        ort_tolerance: typing.Optional[float] = None,
    ) -> bool:
        return self.is_at_position(
            target.position, pos_tolerance
        ) and self.is_at_orientation(target.orientation, ort_tolerance)
