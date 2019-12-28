import kinematics2d as k2d


class TestPose:
    def test_init_default(self) -> None:
        p1 = k2d.Pose(k2d.Vector(24.42, 42.24), 1.221)
        assert (
            p1.position.x == 24.42
            and p1.position.y == 42.24
            and p1.orientation == 1.221
        )

        p2 = k2d.Pose(k2d.Vector(24, 42), 1)
        assert p2.position.x == 24 and p2.position.y == 42 and p2.orientation == 1

    def test_init_from_copy(self) -> None:
        p1 = k2d.Pose(k2d.Vector(24, 42), 1)
        p2 = k2d.Pose.from_copy(p1)
        assert p2.position.x == 24 and p2.position.y == 42 and p2.orientation == 1

    def test_init_zeros(self) -> None:
        p = k2d.Pose.zeros()
        assert p.position.x == 0.0 and p.position.y == 0.0 and p.orientation == 0.0

    def test_getters(self) -> None:
        p = k2d.Pose(k2d.Vector(24, 42), 1.2)
        assert p.position.x == 24
        assert p.position.y == 42
        assert p.orientation == 1.2

    def test_setters(self) -> None:
        p = k2d.Pose(k2d.Vector(24, 42), 1.2)
        p.position.x = 12
        p.position.y = 21
        p.orientation = 0.6
        assert p.position.x == 12
        assert p.position.y == 21
        assert p.orientation == 0.6

    def test_repr(self) -> None:
        p = k2d.Pose(k2d.Vector(24.42, 42.24), 1.221)
        p_repr = "Pose(pos: {}, ort: 1.221)".format(str(p.position))
        assert str(p) == p_repr

    def test_add(self) -> None:
        p1 = k2d.Pose(k2d.Vector(2.2, 3.3), k2d.PI / 2)
        p2 = k2d.Pose(k2d.Vector(3.3, 2.2), k2d.PI)
        p3 = k2d.Pose(k2d.Vector(0.0, 6.6), k2d.PI * 3 / 2)
        assert (p1 + p2).is_at(p3)

        p1 += p2
        assert (p1).is_at(p3)

    def test_sub(self) -> None:
        p1 = k2d.Pose(k2d.Vector(2.2, 3.3), k2d.PI)
        p2 = k2d.Pose(k2d.Vector(2.2, 3.3), k2d.PI)
        p3 = k2d.Pose(k2d.Vector(0.0, 0.0), 0.0)
        assert (p1 - p2).is_at(p3)

        p1 -= p2
        assert (p1).is_at(p3)

    def test_is_at_position(self) -> None:
        p = k2d.Pose(k2d.Vector(2.2, 3.3), 1.1)

        v1 = k2d.Vector(2.2 + k2d.EPSILON / 2, 3.3 - +k2d.EPSILON / 2)
        assert p.is_at_position(v1)

        v2 = k2d.Vector(2.22, 3.33)
        assert p.is_at_position(v2, tolerance=0.1)

        v3 = k2d.Vector(2.3, 3.2)
        assert not p.is_at_position(v3)

        v4 = k2d.Vector(2.4, 3.1)
        assert not p.is_at_position(v4, tolerance=0.1)

    def test_is_at_orientation(self) -> None:
        p = k2d.Pose(k2d.Vector(2.2, 3.3), 1.1)
        assert p.is_at_orientation(1.1 + k2d.EPSILON / 2)
        assert p.is_at_orientation(1.2, tolerance=0.1)
        assert not p.is_at_orientation(1.2)
        assert not p.is_at_orientation(1.3, tolerance=0.1)

    def test_is_at(self) -> None:
        p1 = k2d.Pose(k2d.Vector(2.2, 3.3), 1.1)

        p2 = k2d.Pose(
            k2d.Vector(2.2 + k2d.EPSILON / 2, 3.3 - +k2d.EPSILON / 2),
            1.1 + k2d.EPSILON / 2,
        )
        assert p1.is_at(p2)

        p3 = k2d.Pose(k2d.Vector(2.22, 3.33), 1.2)
        assert p1.is_at(p3, pos_tolerance=0.1, ort_tolerance=0.1)

        p4 = k2d.Pose(k2d.Vector(2.3, 3.2), 1.2)
        assert not p1.is_at(p4)

        p5 = k2d.Pose(k2d.Vector(2.4, 3.1), 1.3)
        assert not p1.is_at(p5, pos_tolerance=0.1, ort_tolerance=0.1)
