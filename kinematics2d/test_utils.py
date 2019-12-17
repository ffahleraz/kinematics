import kinematics2d as k2d


class TestUtils:
    def test_is_close(self) -> None:
        assert k2d.is_close(1.0, 1.0 + k2d.EPSILON / 2)
        assert not k2d.is_close(1.0, 1.0 + k2d.EPSILON * 2)

    def test_rad_from_deg(self) -> None:
        assert k2d.is_close(k2d.rad_from_deg(180), k2d.PI)
        assert k2d.is_close(k2d.rad_from_deg(-90), -k2d.PI / 2)

    def test_deg_from_rad(self) -> None:
        assert k2d.is_close(-k2d.PI, k2d.rad_from_deg(-180))
        assert k2d.is_close(k2d.PI / 2, k2d.rad_from_deg(90))

    def test_angle_cap(self) -> None:
        assert k2d.is_close(k2d.angle_cap(2.22), 2.22)
        assert k2d.is_close(k2d.angle_cap(4.44), -2 * k2d.PI + 4.44)

    def test_angle_diff(self) -> None:
        assert k2d.is_close(k2d.angle_diff(2.22, 1.11), 1.11)
        assert k2d.is_close(k2d.angle_diff(1.11, 2.22), -1.11)
        assert k2d.is_close(k2d.angle_diff(0.11, 2 * k2d.PI - 0.11), 0.22)
        assert k2d.is_close(k2d.angle_diff(2 * k2d.PI - 0.11, 0.11), -0.22)
