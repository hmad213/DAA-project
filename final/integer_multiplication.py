def karatsuba(x, y):
    # Base case
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2
    base = 10 ** m

    # Divide
    a, b = divmod(x, base)
    c, d = divmod(y, base)

    # Conquer
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    abcd = karatsuba(a + b, c + d)

    temp = abcd - ac - bd
    return ac * 10 ** (2 * m) + temp * base + bd