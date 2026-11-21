def count_inversions(A: list) -> int:
    n = len(A)
    if(n <= 1):
        return 0

    mid = n // 2
    B = A[:mid]
    C = A[mid:]
    count = count_inversions(B)
    count += count_inversions(C)
    count += merge_count(A, B, C)
    return count

def merge_count(A: list, B: list, C: list) -> int:
    i = j = k = 0
    count = 0

    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
            count += len(B) - i
        k += 1

    while i < len(B):
        A[k] = B[i]
        i += 1
        k += 1
    while j < len(C):
        A[k] = C[j]
        j += 1
        k += 1

    return count

def test():
    A = [2, 4, 1, 3, 5]
    print(count_inversions(A))

test()