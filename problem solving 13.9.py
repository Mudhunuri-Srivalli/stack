# Find Maximum Element (with Explanation)
def find_max_min_sum(list1):
    # initialize with first element of list
    max_elem = list1[0]
    min_elem = list1[0]
    total = 0

    for i in list1:
        total += i
        if i > max_elem:
            max_elem = i
        if i < min_elem:
            min_elem = i

    print("List:", list1)
    print("Sum =", total)
    print("Maximum =", max_elem)
    print("Minimum =", min_elem)


# Example list
list1 = [1, 2, 3, 4, 5, 9, -32, -45]
find_max_min_sum(list1)

