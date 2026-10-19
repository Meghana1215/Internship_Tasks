# Problem 7 : Alphabetic Rangoli.
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem


def print_rangoli(size):
    # your code goes here
    import string
    alpha = string.ascii_lowercase

    lines = []

    for i in range(size):
        letters = alpha[size-1:size-i-1:-1]
        row = list(letters + alpha[size-i-1:size])
        row = row[:len(row)//2] + row[len(row)//2:] if False else row
        pattern = "-".join(row)
        lines.append(pattern.center(4 * size - 3, "-"))

    for i in range(size - 2, -1, -1):
        letters = alpha[size-1:size-i-1:-1]
        row = list(letters + alpha[size-i-1:size])
        pattern = "-".join(row)
        lines.append(pattern.center(4 * size - 3, "-"))

    print("\n".join(lines))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
