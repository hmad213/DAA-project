import sys

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

def main():
    if len(sys.argv) < 2:
        print("Usage: python int_mul.py <file path>")
        return

    file_path = sys.argv[1]
    numbers = []

    try:
        with open(file_path, "r") as file:
            for line in file:
                if(line.strip()):
                    numbers.append(int(line))

        if(len(numbers) != 2):
            raise ValueError("File must have 2 numbers!")
        print(f"Answer: {karatsuba(numbers[0], numbers[1])}")
    except FileNotFoundError:
        print(f"File path not found: {file_path}")

if __name__ == "__main__":
    main()