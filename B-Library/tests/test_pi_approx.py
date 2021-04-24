from math import pi

from pi_approx import __version__, approximate_pi


def test_version() -> None:
    assert __version__


def test_approx() -> None:
    assert (approximate_pi(300) - pi) < 0.1
