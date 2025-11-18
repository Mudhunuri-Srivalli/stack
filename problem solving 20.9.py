# Wap to check if each number in an list contains duplicate digits, returning true for duplicates and false for unique digits. Input: [202,89,112,88] Output:[true ,false ,true ,true]
def check_duplicate_digits(nums):
    result = []
    for num in nums:
        digits = str(num)         # Convert number to string
        if len(set(digits)) < len(digits):
            result.append(True)    # Duplicate found
        else:
            result.append(False)   # All digits unique
    return result

# Example
nums = [202, 89, 112, 88]
print(check_duplicate_digits(nums))  # Output: [True, False, True, True]

# Sum of All Numbers in a Matrix
def sum_of_matrix(matrix):
    total = 0
    for row in matrix:
        for num in row:
            total += num
    return total

# Example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(sum_of_matrix(matrix))  # Output: 45
