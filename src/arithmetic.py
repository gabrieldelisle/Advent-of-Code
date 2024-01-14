def gcd(numbers: list[int]) -> int:
    """Greater Common Divisor"""
    if len(numbers) == 1:
        return numbers[0]

    b, a = numbers[0], gcd(numbers[1:])
    if b > a:
        a, b = b, a

    while b > 0:
        r = a % b
        a, b = b, r
    return a


def lcm(numbers: list[int]) -> int:
    """Lower Common Divisor"""
    if len(numbers) == 1:
        return numbers[0]
    else:
        a = lcm(numbers[1:])
        return a * numbers[0] // gcd([a, numbers[0]])


def bezout(a: int, b: int) -> int:
    """Solve for integers u and v the following equation
    a * u + b * v = gcd(a,b)

    Note: Solutions are of form
    u = u + k * b // gcd
    v = v - k * a // gcd
    """
    reverse = False
    if b > a:
        reverse = True
        a, b = b, a

    pile = []
    while b > 0:
        q, r = divmod(a, b)
        pile.append(q)
        a, b = b, r
    gcd = a

    u, v = 1, 0
    for q in reversed(pile):
        u, v = v, u - q * v

    if reverse:
        u, v = v, u
    return gcd, u, v


def bezout_extended(a: list[int]):
    """
    Solve for (xn) the equation
    sum(xi * ai) = gcd(ai)

    Using recursive bezout : gn = un * gn-1 + vn * an
    """
    g = a[0]
    uvs = []
    for b in a[1:]:
        g, u, v = bezout(g, b)
        print(g, u, v)
        uvs.append((u, v))

    t = 1
    xs = []
    for u, v in reversed(uvs):
        xs.append(t * v)
        t *= u

    xs.append(t)

    return g, list(reversed(xs))


def diophantine(a: list[int], b: list[int]) -> int:
    """
    Solve system of equations for minimal x where xi are unkwown positive integers :
    a1 * x1 + b1 = x
    .
    .
    .
    an * xn + bn = x
    """
    a0, b0 = a[0], b[0]

    for ai, bi in zip(a[1:], b[1:]):
        g, u, _ = bezout(a0, ai)
        q, r = divmod(bi - b0, g)
        if r != 0:
            raise Exception("No solution")
        a0, b0 = a0 * ai // g, b0 + a0 * ((u * q) % (ai // g))

    return b0, a0


if __name__ == "__main__":
    print(diophantine([99, 97, 95], [49, 76, 65]))
