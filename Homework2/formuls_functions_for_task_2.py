from math import factorial as f

def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            v = func(*args, **kwargs)
        except Exception:
            return 0
        return int(v)
    return wrapper

@catch_errors
def a1(k, n):
    return f(k) / f(n) / f(k - n)


@catch_errors
def a2(k, n):
    return f(n - 1) / f(k - 1) / f(n - k)


@catch_errors
def a3(k, n):
    return f(n + k - 1) / f(k - 1) / f(n)


@catch_errors
def b1(k, n):
    return 0 if n > k else 1


@catch_errors
def b2(k, n):
    if n <= 0:
        return 1
    if k <= 0:
        return 0
    if k == 0 and n== 0:
        return -1
    if n == k:
        return 1
    if n < k:
        return 0
    return k * b2(k, n - 1) + b2(k - 1, n - 1)


@catch_errors
def b3(k, n):
    return sum([b2(i, n) for i in range(1, k)])


@catch_errors
def c1(k, n):
    return f(k) / f(k - n)


@catch_errors
def c2(k, n):
    return a2(k, n) * f(n)


@catch_errors
def c3(k, n):
    return k**n


@catch_errors
def d1(k, n):
    return b1(k, n)


@catch_errors
def d2(k, n, c=0):
    if c > 100:
        return 0
    if k == 0:
        return 0
    if k == n:
        return 1
    return d2(k, n - k, c + 1) + d2(k - 1, n - 1, c + 1)


@catch_errors
def d3(k, n):
    return sum([d2(i, n) for i in range(1, k)])

















    
