import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def brute_force(points):
    min_dist, best = float('inf'), None
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            d = dist(points[i], points[j])
            if(d < min_dist):
                min_dist, best = d, (points[i], points[j])

    return min_dist, best


def strip_closest(strip, d):
    min_dist, best = d, None
    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_dist:
                break
            new_d = dist(strip[i], strip[j])
            if(new_d < min_dist):
                min_dist, best = new_d, (strip[i], strip[j])

    return min_dist, best

def closest_rec(points):
    n = len(points)

    if n <= 3:
        return brute_force(points)

    mid = n // 2
    mid_point = points[mid]

    dl, bl = closest_rec(points[:mid])
    dr, br = closest_rec(points[mid:])

    d = min(dl, dr)

    strip = [p for p in points if abs(p[0] - mid_point[0]) < d]

    sd, sb = strip_closest(strip, d)

    if(d > sd):
        return sd, sb
    
    if(d == dl):
        return dl, bl
    return dr, br


def closest(points):
    points.sort()
    return closest_rec(points)