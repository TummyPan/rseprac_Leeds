import numpy as np


def primes(n):
    numbers = np.arange(2, n + 1)
    mask = np.prod(
        [(numbers == j) + (numbers % j != 0) for j in numbers], dtype=bool, axis=0
    )
    return [] if n < 2 else list(numbers[mask])


print(primes(100))
