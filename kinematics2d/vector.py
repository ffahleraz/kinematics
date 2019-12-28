import math
import typing

import numpy as np

import kinematics2d as k2d

__all__ = ["Vector"]


class Vector:
    """A 2-dimensional vector.

    Attributes:
        - x: float
        - y: float
    """

    def __init__(self, x: float, y: float) -> None:
        self._ndarray: np.ndarray = np.array([x, y]).astype(float)

    @classmethod
    def from_copy(cls, source: "Vector") -> "Vector":
        return cls.from_ndarray(source._ndarray)

    @classmethod
    def zeros(cls) -> "Vector":
        return cls(0.0, 0.0)

    @classmethod
    def from_ndarray(cls, array: np.ndarray) -> "Vector":
        return cls(array[0], array[1])

    @property
    def x(self) -> float:
        return self._ndarray[0]

    @x.setter
    def x(self, value: float) -> None:
        self._ndarray[0] = value

    @property
    def y(self) -> float:
        return self._ndarray[1]

    @y.setter
    def y(self, value: float) -> None:
        self._ndarray[1] = value

    def __repr__(self) -> str:
        return "Vector(x: {}, y: {})".format(self._ndarray[0], self._ndarray[1])

    def __add__(self, other: "Vector") -> "Vector":
        return Vector.from_ndarray(self._ndarray + other._ndarray)

    def __radd__(self, other: "Vector") -> "Vector":
        return other + self

    def __iadd__(self, other: "Vector") -> "Vector":
        return self + other

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector.from_ndarray(self._ndarray - other._ndarray)

    def __rsub__(self, other: "Vector") -> "Vector":
        return other - self

    def __isub__(self, other: "Vector") -> "Vector":
        return self - other

    def __mul__(self, other: float) -> "Vector":
        return Vector.from_ndarray(self._ndarray * other)

    def __imul__(self, other: float) -> "Vector":
        return self * other

    def __truediv__(self, other: float) -> "Vector":
        return Vector.from_ndarray(self._ndarray / other)

    def __itruediv__(self, other: float) -> "Vector":
        return self / other

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return (
            self._ndarray[0] == other._ndarray[0]
            and self._ndarray[1] == other._ndarray[1]
        )

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return (
            self._ndarray[0] != other._ndarray[0]
            or self._ndarray[1] != other._ndarray[1]
        )

    def __neg__(self) -> "Vector":
        return Vector.from_ndarray(-self._ndarray)

    def __abs__(self) -> float:
        return self.magnitude

    def __hash__(self):
        return hash((self.x, self.y))

    def is_close_to(
        self, other: "Vector", epsilon: typing.Optional[float] = None
    ) -> bool:
        return k2d.is_close(self.x, other.x, epsilon) and k2d.is_close(
            self.y, other.y, epsilon
        )

    @property
    def magnitude(self) -> float:
        return np.linalg.norm(self._ndarray)

    @property
    def angle(self) -> float:
        return math.atan2(self._ndarray[1], self._ndarray[0])

    def angle_from(self, other: "Vector") -> float:
        if abs(self) == 0.0 or abs(other) == 0.0:
            return 0.0
        else:
            cos = other.dot(self) / (abs(other) * abs(self))
            return math.acos(round(cos, 4))

    def dot(self, other: "Vector") -> float:
        return np.dot(self._ndarray, other._ndarray)

    def rotated(self, angle: float) -> "Vector":
        rotation_matrix = np.array(
            [
                [math.cos(angle), -1 * math.sin(angle)],
                [math.sin(angle), math.cos(angle)],
            ]
        )
        return Vector.from_ndarray(np.dot(rotation_matrix, self._ndarray))

    def normalized(self) -> "Vector":
        magnitude = self.magnitude
        if magnitude != 0.0:
            return self / magnitude
        else:
            return Vector.zeros()

    def projected_to(self, other: "Vector") -> "Vector":
        if abs(other) == 0.0:
            return Vector.zeros()
        else:
            return other.normalized() * self.dot(other) / abs(other)
