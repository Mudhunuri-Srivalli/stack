# Convert Diagonal Elements to Zero
def convert_diagonals_to_zero(matrix):
    n = len(matrix)  # number of rows (square matrix)

    for i in range(n):
        for j in range(n):
            # Check for left diagonal (i == j)
            # OR right diagonal (i + j == n - 1)
            if i == j or (i + j == n - 1):
                matrix[i][j] = 0
    return matrix


# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in matrix:
    print(row)

# Convert diagonals to zero
result = convert_diagonals_to_zero(matrix)

print("\nMatrix after converting diagonals to zero:")
for row in result:
    print(row)

