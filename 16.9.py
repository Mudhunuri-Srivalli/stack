# 1. Bubble Sort in Descending Order (for numbers)
def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:  # Change comparison for descending order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example Usage
numbers = [5, 1, 9, 3, 7]
sorted_numbers = bubble_sort_desc(numbers)
print("Descending Order:", sorted_numbers)

# 2. Bubble Sort to Sort Strings Alphabetically
def bubble_sort_strings(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  # Compare strings alphabetically
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example Usage
string_list = ["apple", "banana", "grape", "cherry"]
sorted_strings = bubble_sort_strings(string_list)
print("Alphabetically Sorted Strings:", sorted_strings)

#  3. Bubble Sort Strings Based on Length (Shortest to Longest)
def bubble_sort_by_length(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if len(arr[j]) > len(arr[j + 1]):  # Compare based on length
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example Usage
string_list = ["apple", "banana", "kiwi", "cherry", "fig"]
sorted_by_length = bubble_sort_by_length(string_list)
print("Sorted by Length:", sorted_by_length)

# 4. Bubble Sort Nested Lists Based on First Element
def bubble_sort_nested_lists(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j][0] > arr[j + 1][0]:  # Compare first elements of nested lists
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example Usage
nested_list = [[3, 'apple'], [1, 'banana'], [2, 'cherry']]
sorted_nested = bubble_sort_nested_lists(nested_list)
print("Sorted Nested Lists:", sorted_nested)

# Sample Output Example
# Descending Order: [9, 7, 5, 3, 1]
# Alphabetically Sorted Strings: ['apple', 'banana', 'cherry', 'grape']
# Sorted by Length: ['fig', 'kiwi', 'apple', 'grape', 'banana']
# Sorted Nested Lists: [[1, 'banana'], [2, 'cherry'], [3, 'apple']]