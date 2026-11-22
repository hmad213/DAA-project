def quicksort(A: list, left: int, right: int):
    if left < right:
        s = partition(A, left, right)
        quicksort(A, left, s - 1)
        quicksort(A, s + 1, right)


def partition(A, l, r):
    p = A[r]
    i = l - 1
    for j in range(l, r):
        if A[j] <= p:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort_helper(A: list):
    quicksort(A, 0, len(A) - 1)

def test():
    A = [5, 1, 2, 8, 6, 3, 0, 9, 7, 4]
    quicksort_helper(A)
    print(A)

test()