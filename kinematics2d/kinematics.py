import math
from typing import Optional

import kinematics2d as k2d

__all__ = ["Kinematics"]


class Kinematics:
    """A 2-dimensional kinematics.

    Attributes:
        - position: k2d.Vector
        - orientation: float (in radians)
        - velocity: k2d.Vector
        - rotation: float (in radians)
    """

    def __init__(
        self,
        position: k2d.Vector,
        orientation: float,
        velocity: k2d.Vector,
        rotation: float,
    ) -> None:
        self._position: k2d.Vector = k2d.Vector.from_copy(position)
        self._orientation: float = orientation
        self._velocity: k2d.Vector = k2d.Vector.from_copy(velocity)
        self._rotation: float = rotation

    @classmethod
    def from_pose(
        cls, pose: k2d.Pose, velocity: k2d.Vector, rotation: float
    ) -> "Kinematics":
        return cls(pose.position, pose.orientation, velocity, rotation)

    @classmethod
    def from_copy(cls, source: "Kinematics") -> "Kinematics":
        return cls(
            k2d.Vector.from_copy(source.position),
            source.orientation,
            k2d.Vector.from_copy(source.velocity),
            source.rotation,
        )

    @classmethod
    def zeros(cls) -> "Kinematics":
        return cls.from_pose(k2d.Pose.zeros(), k2d.Vector.zeros(), 0.0)

    @property
    def pose(self) -> k2d.Pose:
        return k2d.Pose(self._position, self._orientation)

    @property
    def position(self) -> k2d.Vector:
        return self._position

    @position.setter
    def position(self, value: k2d.Vector) -> None:
        self._position = value

    @property
    def orientation(self) -> float:
        return self._orientation

    @orientation.setter
    def orientation(self, value: float) -> None:
        self._orientation = value

    @property
    def velocity(self) -> k2d.Vector:
        return self._velocity

    @velocity.setter
    def velocity(self, value: k2d.Vector) -> None:
        self._velocity = value

    @property
    def rotation(self) -> float:
        return self._rotation

    @rotation.setter
    def rotation(self, value: float) -> None:
        self._rotation = value

    def __repr__(self) -> str:
        return "Kinematics(pos: {}, ort: {}, vel: {}, rot: {})".format(
            self.position, self.orientation, self.velocity, self.rotation
        )

    def __add__(self, other: "Kinematics") -> "Kinematics":
        """Calculate the transformation of other to the coordinate frame of self."""
        return Kinematics(
            self.position + other.position.rotated(self.orientation),
            self.orientation + other.orientation,
            self.velocity + other.velocity.rotated(self.orientation),
            self.rotation + other.rotation,
        )

    def __sub__(self, other: "Kinematics") -> "Kinematics":
        """Calculate the transformation of self to the coordinate frame of other."""
        return Kinematics(
            (self.position - other.position).rotated(-other.orientation),
            self.orientation - other.orientation,
            (self.velocity - other.velocity).rotated(-other.orientation),
            self.rotation - other.rotation,
        )

    def updated(self, delta_time: float) -> "Kinematics":
        delta_orientation = self.rotation * delta_time
        new_orientation = self.orientation + delta_orientation
        delta_position = self.velocity * delta_time
        new_position = self.position + delta_position.rotated(delta_orientation)
        return Kinematics(new_position, new_orientation, self.velocity, self.rotation)

    def delta_position_to_stop(self, max_linear_decel_magnitude: float) -> k2d.Vector:
        return (
            self.velocity.normalized()
            * (abs(self.velocity) ** 2)
            / (2.0 * max_linear_decel_magnitude)
        )

    def delta_orientation_to_stop(self, max_angular_decel_magnitude: float) -> float:
        value = (abs(self.rotation) ** 2) / (2.0 * max_angular_decel_magnitude)
        return value if self.rotation > 0.0 else -value
