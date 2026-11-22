def min_max(A: list, low: int, high: int) -> tuple:
    if(low >= high):
        return (A[low], A[high])

    mid = (high + low) // 2
    min1, max1 = min_max(A, low, mid)
    min2, max2 = min_max(A, mid + 1, high)

    return (min(min1, min2), max(max1, max2))

def min_max_helper(A: list) -> tuple:
    return min_max(A, 0, len(A) - 1)


def test():
    A = [5, 1, 2, 8, 6, 3, 0, 9, 7, 4]
    print(min_max_helper(A))

test()