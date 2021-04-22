def approximate_pi(iteration_count: int) -> float:
    sign = 1
    result = 0.0
    for at in range(iteration_count):
        part = sign / (2 * at + 1)
        result += part
        sign = -1 if sign == 1 else 1
    return result * 4


if __name__ == "__main__":
    from math import pi
    from timeit import timeit

    print(timeit(stmt="approximate_pi(1000)", number=10000, globals=globals()))

    approx = approximate_pi(1000)
    print(f"approx {approx} with diff {approx - pi}")
