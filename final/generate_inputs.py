import os
import random

SIZES = [101, 125, 150, 200, 300, 450, 650, 900, 1200, 1500]


def random_n_digit_int(digits):
    first = str(random.randint(1, 9))
    rest = "".join(random.choices("0123456789", k=digits - 1))
    return first + rest


def generate_closest_pair_file(filepath, n):
    max_coord = 100 * n
    points = set()
    while len(points) < n:
        points.add((random.randint(0, max_coord), random.randint(0, max_coord)))

    with open(filepath, "w", newline="\n") as f:
        f.write(f"{n}\n")
        for x, y in points:
            f.write(f"{x} {y}\n")


def generate_integer_mult_file(filepath, digits):
    num1 = random_n_digit_int(digits)
    num2 = random_n_digit_int(digits)
    with open(filepath, "w", newline="\n") as f:
        f.write(f"{num1}\n{num2}\n")


def main():
    current_dir = os.getcwd()
    base_dir = os.path.join(current_dir, "inputs")
    cp_dir = os.path.join(base_dir, "closest_pair")
    im_dir = os.path.join(base_dir, "integer_mult")

    os.makedirs(cp_dir, exist_ok=True)
    os.makedirs(im_dir, exist_ok=True)

    for idx, size in enumerate(SIZES):
        filename = f"{idx+1}.txt"
        generate_closest_pair_file(os.path.join(cp_dir, filename), size)
        generate_integer_mult_file(os.path.join(im_dir, filename), size)

    print(f"Generated 20 input files inside: {base_dir}")


if __name__ == "__main__":
    main()