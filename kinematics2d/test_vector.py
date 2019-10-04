import numpy as np

import kinematics2d as km


class TestVector:
    def test_init_default(self) -> None:
        v1 = km.Vector(3.3333, 6.6666)
        assert v1.x == 3.3333 and v1.y == 6.6666

        v2 = km.Vector(40, 50)
        assert v2.x == 40.0 and v2.y == 50.0

    def test_init_from_array(self) -> None:
        v = km.Vector.from_array(np.array([36.666, 72.222]))
        assert v.x == 36.666 and v.y == 72.222

    def test_init_from_copy(self) -> None:
        v1 = km.Vector(1.1111, 2.2222)
        v2 = km.Vector.from_copy(v1)
        assert v2.x == v1.x and v2.y == v1.y

    def test_init_zeros(self) -> None:
        v = km.Vector.zeros()
        assert v.x == 0.0 and v.y == 0.0

    def test_setters(self) -> None:
        v = km.Vector(24, 42)
        v.x = 12
        v.y = 21
        assert v.x == 12 and v.y == 21

