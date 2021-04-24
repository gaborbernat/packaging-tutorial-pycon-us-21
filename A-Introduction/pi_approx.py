# pi_approx.py
from math import pi


def approximate_pi(iteration_count: int) -> float:
    sign, result = 1, 0.0
    for at in range(iteration_count):
        result += sign / (2 * at + 1)
        sign *= -1
    return result * 4


if __name__ == "__main__":
    approx_1, approx_2 = approximate_pi(300), approximate_pi(301)
    print(f"approx 300 {approx_1} with diff {approx_1 - pi}")
    print(f"approx 301 {approx_2} with diff {approx_2 - pi}")
