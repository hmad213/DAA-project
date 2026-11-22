def power(a: float, n: int) -> float:
    if n == 0:
        return 1

    if n == 1:
        return a

    half = power(a, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return half * half * a

def test():
    print(power(2, 15))
    print(power(3, 4))
    print(power(1.5, 3))

test()