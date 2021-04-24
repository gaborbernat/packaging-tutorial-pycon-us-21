from .__version__ import __version__


def approximate_pi(iteration_count: int) -> float:
    """
    Approximate the number 𝜋.

    :param iteration_count: the number of iterations to run
    :return: the approximation
    """
    sign, result = 1, 0.0
    for at in range(iteration_count):
        result += sign / (2 * at + 1)
        sign *= -1
    return result * 4


__all__ = (
    "__version__",
    "approximate_pi",
)
