from functools import lru_cache


@lru_cache(10000)
def r1(x):
    if x == 0:
        return 2
    return r1(x - 1) + x


@lru_cache(10000)
def r2(x):
    if x == 0:
        return 1
    return 2 * r2(x - 1) + 2


@lru_cache(10000)
def r3(x):
    if x == 0:
        return 5
    return 3 * r3(x - 1) + 2**x


@lru_cache(10000)
def r4(x):
    if x == 0:
        return 1
    if x == 1:
        return 17
    return 4 * r4(x - 1) + 5 * r4(x - 2)


@lru_cache(10000)
def r5(x):
    if x == 0:
        return 3
    if x == 1:
        return 11
    return 4 * r5(x - 1) - 4 * r5(x - 2)


@lru_cache(10000)
def r6(x):
    if x == 0:
        return 3
    if x == 1:
        return 2
    if x == 2:
        return 6
    return 2 * r6(x - 1) + r6(x - 2) - 2 * r6(x - 3)
