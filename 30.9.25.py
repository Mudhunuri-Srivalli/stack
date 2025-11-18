
#Binary search using recursion
#Max element in a list

# 1. Binary Search using Recursion
def binary_search(arr, low, high, target):
    if low > high:
        return -1  # Element not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)


# Example usage:
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(arr, 0, len(arr) - 1, target)
print("Binary Search Result:", result)  # Output: 3





# 2. Find Maximum Element in a List using Recursion
def find_max(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n - 1], find_max(arr, n - 1))


# Example usage:
arr = [12, 5, 87, 34, 56, 99, 23]
print("Maximum Element:", find_max(arr, len(arr)))  # Output: 99
