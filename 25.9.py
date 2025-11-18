# Check if the given matrix is an identity matrix
# def is_identity_matrix(matrix):
#     n = len(matrix)
#     for i in range(n):
#         for j in range(n):
#             if i == j and matrix[i][j] != 1:   # diagonal must be 1
#                 return False
#             elif i != j and matrix[i][j] != 0: # non-diagonal must be 0
#                 return False
#     return True


# mat = [[1,0,0],[0,1,0],[0,0,1]]
# print("Identity Matrix:", is_identity_matrix(mat))


# Add 2 matrixs
# def add_matrices(a, b):
#     result = []
#     for i in range(len(a)):
#         row = []
#         for j in range(len(a[0])):
#             row.append(a[i][j] + b[i][j])
#         result.append(row)
#     return result


# A = [[1,2,3],[4,5,6],[7,8,9]]
# B = [[9,8,7],[6,5,4],[3,2,1]]
# print("Matrix Addition:")
# for row in add_matrices(A,B):
#     print(row)


# Sum of diagonal elements =>
# def sum_of_diagonals(matrix):
#     n = len(matrix)
#     left_diag = sum(matrix[i][i] for i in range(n))
#     right_diag = sum(matrix[i][n-i-1] for i in range(n))
#     return left_diag + right_diag


# mat = [[1,2,3],[4,5,6],[7,8,9]]
# print("Sum of Diagonal Elements:", sum_of_diagonals(mat))


# . Matrix multiplication
# def multiply_matrices(a, b):
#     result = [[0]*len(b[0]) for _ in range(len(a))]
#     for i in range(len(a)):
#         for j in range(len(b[0])):
#             for k in range(len(b)):
#                 result[i][j] += a[i][k] * b[k][j]
#     return result


# A = [[1,2,3],[4,5,6],[7,8,9]]
# B = [[9,8,7],[6,5,4],[3,2,1]]
# print("Matrix Multiplication:")
# for row in multiply_matrices(A,B):
#     print(row)


# Transpose of a matrix
def transpose(matrix):
    result = [[0]*len(matrix) for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result


A = [[1,2,3],[4,5,6],[7,8,9]]
print("Transpose of Matrix:")
for row in transpose(A):
    print(row)

