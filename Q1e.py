def find_kth_smallest(numbers, k):
    pivot = numbers[-1]
    smaller = []
    larger = []
    equal_count = 0

    for x in numbers:
        if x < pivot:
            smaller.append(x)
        elif x > pivot:
            larger.append(x)
        else:
            equal_count += 1

    if k < len(smaller):
        return find_kth_smallest(smaller, k)
    if k < len(smaller) + equal_count:
        return pivot
    return find_kth_smallest(larger, k - len(smaller) - equal_count)


def closest_in_group(numbers):
    count = len(numbers)
    if count == 1:
        return numbers[0], numbers[0], float("inf"), None
    if count == 2:
        low, high = min(numbers), max(numbers)
        return low, high, high - low, (low, high)

    median = find_kth_smallest(numbers, count // 2)

    left_group = []
    right_group = []
    median_count = 0
    for x in numbers:
        if x < median:
            left_group.append(x)
        elif x > median:
            right_group.append(x)
        else:
            median_count += 1

    if median_count >= 2:
        return median, median, 0, (median, median)

    left_group.append(median)

    left_min, left_max, left_gap, left_pair = closest_in_group(left_group)
    right_min, right_max, right_gap, right_pair = closest_in_group(right_group)
    middle_gap = right_min - left_max
    middle_pair = (left_max, right_min)

    best_gap, best_pair = min(
        (left_gap, left_pair),
        (right_gap, right_pair),
        (middle_gap, middle_pair),
        key=lambda candidate: candidate[0],
    )
    return left_min, right_max, best_gap, best_pair


def find_closest_pair(numbers):
    _, _, smallest_gap, closest_pair = closest_in_group(numbers)
    return smallest_gap, closest_pair


if __name__ == "__main__":
    data = [8.5, 1.0, 14.2, 3.1, 9.0, 20.0, 2.5]
    print(find_closest_pair(data))