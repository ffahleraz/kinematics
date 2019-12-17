import numpy as np

import kinematics2d as km


class TestVector:
    def test_init_default(self) -> None:
        v1 = km.Vector(24.42, 42.24)
        assert v1.x == 24.42 and v1.y == 42.24

        v2 = km.Vector(24, 42)
        assert v2.x == 24.0 and v2.y == 42.0

    def test_init_from_copy(self) -> None:
        v1 = km.Vector(24, 42)
        v2 = km.Vector.from_copy(v1)
        assert v2.x == v1.x and v2.y == v1.y

    def test_init_zeros(self) -> None:
        v = km.Vector.zeros()
        assert v.x == 0.0 and v.y == 0.0

    def test_init_from_ndarray(self) -> None:
        v = km.Vector.from_ndarray(np.array([24, 42]))
        assert v.x == 24 and v.y == 42

    def test_setters(self) -> None:
        v = km.Vector(24, 42)
        v.x = 12
        v.y = 21
        assert v.x == 12 and v.y == 21

    def test_repr(self) -> None:
        v = km.Vector(24.42, 42.24)
        v_repr = "Vector(x: 24.42, y: 42.24)"
        assert str(v) == v_repr

    def test_add(self) -> None:
        v1 = km.Vector(2.2, 1.1)
        v2 = km.Vector(1.1, 2.2)
        v3 = km.Vector(3.3, 3.3)
        assert (v1 + v2).is_close_to(v3)

    def test_sub(self) -> None:
        v1 = km.Vector(2.2, 1.1)
        v2 = km.Vector(1.1, 2.2)
        v3 = km.Vector(1.1, -1.1)
        assert (v1 - v2).is_close_to(v3)

    def test_mul(self) -> None:
        v1 = km.Vector(8, 14)
        v2 = km.Vector(24, 42)
        assert (v1 * 3).is_close_to(v2)

    def test_truediv(self) -> None:
        v1 = km.Vector(24, 42)
        v2 = km.Vector(8, 14)
        assert (v1 / 3).is_close_to(v2)

    def test_eq(self) -> None:
        v1 = km.Vector(24.24, 42.42)
        v2 = km.Vector(24.24, 42.42)
        assert v1 == v2

    def test_ne(self) -> None:
        v1 = km.Vector(24.24, 42.24)
        v2 = km.Vector(24.42, 42.42)
        assert v1 != v2

    def test_neg(self) -> None:
        v = km.Vector(24.42, -42.24)
        v_neg = km.Vector(-24.42, 42.24)
        assert -v == v_neg

    def test_abs(self) -> None:
        v = km.Vector(3.33, 4.44)
        assert km.is_close(abs(v), 5.55)

    def test_hash(self) -> None:
        v = km.Vector(24.42, 42.24)
        assert hash(v) == hash((24.42, 42.24))

    def test_is_close_to(self) -> None:
        v1 = km.Vector(1.0, 1.0)
        v2 = km.Vector(1.00001, 1.00001)
        assert not v1.is_close_to(v2)

        v3 = km.Vector(1.0000000001, 1.0000000001)
        assert v1.is_close_to(v3)

    def test_magnitude(self) -> None:
        v = km.Vector(3.33, 4.44)
        assert km.is_close(abs(v), 5.55)

    def test_angle(self) -> None:
        v1 = km.Vector(2.0, 0.0)
        assert km.is_close(v1.angle, 0.0, 1e-3)

        v2 = km.Vector(0.0, 2.0)
        assert km.is_close(v2.angle, km.PI / 2, 1e-3)

        v3 = km.Vector(-2.0, -2.0)
        assert km.is_close(v3.angle, -km.PI * 6 / 8, 1e-3)

        v4 = km.Vector.zeros()
        assert km.is_close(v4.angle, 0.0, 1e-3)

    def test_angle_from(self) -> None:
        v1 = km.Vector(-2.0, -2.0)
        v2 = km.Vector(0.0, 2.0)
        assert km.is_close(v2.angle_from(v1), km.PI * 6 / 8, 1e-3)

        v3 = km.Vector.zeros()
        v4 = km.Vector.zeros()
        assert km.is_close(v3.angle_from(v4), -0.0, 1e-3)

    def test_dot(self) -> None:
        v1 = km.Vector(2.0, 3.0)
        v2 = km.Vector(3.0, 2.0)
        assert km.is_close(v1.dot(v2), 12.0)

    def test_rotated(self) -> None:
        v1 = km.Vector(2.0, 2.0)
        v2 = km.Vector(-2.0, -2.0)
        assert v1.rotated(km.PI).is_close_to(v2)

    def test_normalized(self) -> None:
        v1 = km.Vector(3.33, 4.44)
        v2 = km.Vector(0.6, 0.8)
        assert v1.normalized().is_close_to(v2)

    def test_projected_to(self) -> None:
        v1 = km.Vector(24.42, 42.24)
        v2 = km.Vector(1.0, 0.0)
        v3 = km.Vector(24.42, 0.0)
        assert v1.projected_to(v2).is_close_to(v3)
