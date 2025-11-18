# Sock Pair Problem
def sock_pairs(socks):
    pairs = 0
    color_count = {}

    # Count how many socks of each color
    for color in socks:
        color_count[color] = color_count.get(color, 0) + 1

    # Each 2 socks make one pair
    for count in color_count.values():
        pairs += count // 2

    return pairs


# Example
socks = ['red', 'green', 'red', 'purple', 'green', 'black', 'red']
print("Days you can sustain:", sock_pairs(socks))

# Find Missing Digits
def find_missing_digits(num):
    all_digits = set('0123456789')
    num_digits = set(str(num))
    missing = sorted(all_digits - num_digits)
    print("Missing digits:", ''.join(missing))
    print("Total missing:", len(missing))


# Example
find_missing_digits(34571)

# Matrix Addition using Range
def add_matrices(mat1, mat2):
    rows = len(mat1)
    cols = len(mat1[0])
    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)

    return result


# Example matrices
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [1, 2, 3]
]

result = add_matrices(A, B)
print("Matrix Addition Result:")
for row in result:
    print(row)

