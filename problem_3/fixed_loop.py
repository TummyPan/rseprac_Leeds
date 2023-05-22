def primes(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []

    s = list(range(3, n + 1, 2))
    for i in range(int((n**0.5 - 3) / 2 + 1)):
        m = 2 * i + 3
        for j in range(int((m * m - 3) / 2), (n + 1) // 2 - 1, m):
            s[j] = 0

    return [2] + [x for x in s if x]


print(primes(100))
