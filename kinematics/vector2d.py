#!/usr/bin/env python3

import math
from typing import Optional, Any

import numpy as np


class Vector2D:
    """
        A class that represents a 2-dimensional vector.
    """

    def __init__(self, x: float, y: float) -> None:
        self._array = np.array([x, y], dtype="Float64")


    @classmethod
    def from_array(cls, array: np.ndarray) -> 'Vector2D':
        return cls(array[0], array[1])


    @classmethod
    def from_copy(cls, source: 'Vector2D') -> 'Vector2D':
        return cls.from_array(source._array)


    @classmethod
    def zero(cls) -> 'Vector2D':
        return cls(0.0, 0.0)


    @property
    def x(self) -> float:
        return self._array[0]


    @x.setter
    def x(self, value: float) -> None:
        self._array[0] = value


    @property
    def y(self) -> float:
        return self._array[1]


    @y.setter
    def y(self, value: float) -> None:
        self._array[1] = value


    @property
    def magnitude(self) -> float:
        return np.linalg.norm(self._array)


    @property
    def unit(self) -> 'Vector2D':
        magnitude = self.magnitude
        if magnitude != 0.0:
            return self / magnitude
        else:
            return Vector2D.zero()


    @property
    def angle(self) -> float:
        return math.atan2(self._array[1], self._array[0])


    def __repr__(self) -> str:
        return "Vector2D(x: {}, y: {})".format(self._array[0], self._array[1])


    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D.from_array(self._array + other._array)


    def __radd__(self, other: 'Vector2D') -> 'Vector2D':
        return self + other


    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D.from_array(self._array - other._array)
        

    def __rsub__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D.from_array(other._array - self._array)
        

    def __mul__(self, other: float) -> 'Vector2D':
        return Vector2D.from_array(self._array * other)


    def __truediv__(self, other: float) -> 'Vector2D':
        return Vector2D.from_array(self._array / other)


    def __eq__(self, other: 'Vector2D') -> bool:  # type: ignore
        return self._array[0] == other._array[0] and \
            self._array[1] == other._array[1]


    def __ne__(self, other: 'Vector2D') -> bool:  # type: ignore
        return self._array[0] != other._array[0] or \
            self._array[1] != other._array[1]


    def __neg__(self) -> 'Vector2D':
        return Vector2D.from_array(-self._array)


    def __abs__(self) -> float:
        return self.magnitude


    def __lt__(self, other: Any) -> bool:
        return abs(self) < abs(other)


    def __hash__(self):
        return hash((self.x, self.y))


    def dot(self, other: 'Vector2D') -> float:
        return np.dot(self._array, other._array)


    def rotate(self, angle: float) -> None:
        rotation_matrix = np.array([
            [math.cos(angle), -1 * math.sin(angle)], 
            [math.sin(angle), math.cos(angle)]
        ])
        self._array = np.dot(rotation_matrix, self._array)


    def rotated(self, angle: float) -> 'Vector2D':
        new_vector = Vector2D.from_copy(self)
        new_vector.rotate(angle)
        return new_vector
    

    def normalize(self, scale: float) -> None:
        self._array = self.unit._array * scale


    def normalized(self, scale: float) -> 'Vector2D':
        new_vector = Vector2D.from_copy(self)
        new_vector.normalize(scale)
        return new_vector


    def project_to(self, other: 'Vector2D') -> None:
        if abs(other) == 0:
            self._array = Vector2D.zero()._array
        else:
            self._array = other.normalized(self.dot(other) / abs(other))._array

    
    def projected_to(self, other: 'Vector2D') -> 'Vector2D':
        new_vector = Vector2D.from_copy(self)
        new_vector.project_to(other)
        return new_vector


    def angle_from(self, other: 'Vector2D') -> float:
        if abs(self) == 0.0 or abs(other) == 0.0:
            return 0.0
        else:
            cos = other.dot(self) / (abs(other) * abs(self))
            return math.acos(round(cos, 4))


    def _raise_unsupported_operand(self,
                                  operator: str,
                                  lhs: Any,
                                  rhs: Any) -> None:
        raise TypeError(
                "unsupported operand type(s) for {}: '{}' and '{}'".format(
                operator, type(lhs), type(rhs)))
