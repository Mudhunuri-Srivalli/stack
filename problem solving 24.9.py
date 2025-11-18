# Check if the Given Matrix is an Identity Matrix
def is_identity(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if (i == j and matrix[i][j] != 1) or (i != j and matrix[i][j] != 0):
                return False
    return True


# Example
mat1 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
print("Is identity matrix:", is_identity(mat1))

# Add Two Matrices
def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] + B[i][j])
        result.append(row)

    return result


# Example
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

sum_matrix = add_matrices(A, B)
print("Matrix Addition Result:")
for row in sum_matrix:
    print(row)

# Sum of Diagonal Elements
def sum_of_diagonals(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        total += matrix[i][i]               # Left diagonal
        if i != n - 1 - i:                  # Avoid double-counting center element (odd n)
            total += matrix[i][n - 1 - i]   # Right diagonal
    return total


# Example
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Sum of diagonal elements:", sum_of_diagonals(mat))

# Matrix Multiplication
def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Multiply
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


# Example
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

product = multiply_matrices(A, B)
print("Matrix Multiplication Result:")
for row in product:
    print(row)

