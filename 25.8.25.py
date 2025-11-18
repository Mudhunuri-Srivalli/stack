#reverse
# list1=[1,2,3,5,9]
# list1.reverse()
# print(list1)

# #sort
# list1=[1,-32,45,62,91,-321]
# list1.sort(reverse=True)
# print(list1)


# list1=['apple','fish','ball','cat','dog','elephant']
# list1.sort()
# print(list1)


# list1=['apple', 'fish','ball','cat','dog','elephant']
# list1.sort(key = len)
# print(list1)


# list1=[[12,2,5,6],[-1,-5,81],[6,7,8]]
# list1.sort(key =lambda l1:(l1[0],l1[1]))
# print(list1)


# count1=(1,-32,45,62,91,-321)
# count1.sort()
# print(count1)


# list1=[1,4,5,[6,7,8]]
# list3=list1.copy()
# print(list3)
# list1[1]=2
# list1[3][0]=8
# print(list3)
# print(list1)


# import copy
# list4=copy.deepcopy(list1)



# Sets & List Inbuilt Functions Examples

# Program: Examples of List & Set Inbuilt Functions in Python

print("========== LIST FUNCTIONS EXAMPLES ==========")

# Sample List
numbers = [10, 20, 30, 40, 20, 50]

print("Original List:", numbers)

# len()
print("Length:", len(numbers))

# append()
numbers.append(60)
print("After append(60):", numbers)

# insert()
numbers.insert(2, 25)
print("After insert(2, 25):", numbers)

# remove()
numbers.remove(20)
print("After remove(20):", numbers)

# pop()
popped = numbers.pop()
print("Popped element:", popped)
print("After pop():", numbers)

# index()
print("Index of 30:", numbers.index(30))

# count()
print("Count of 20:", numbers.count(20))

# sort()
numbers.sort()
print("After sort():", numbers)

# reverse()
numbers.reverse()
print("After reverse():", numbers)

# copy()
copy_list = numbers.copy()
print("Copied list:", copy_list)

# clear()
copy_list.clear()
print("After clear():", copy_list)



print("\n========== SET FUNCTIONS EXAMPLES ==========")

# Sample Sets
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

print("Set A:", setA)
print("Set B:", setB)

# add()
setA.add(7)
print("After add(7) to A:", setA)

# update()
setA.update([8, 9])
print("After update([8, 9]) to A:", setA)

# remove()
setA.remove(2)
print("After remove(2) from A:", setA)

# discard()
setA.discard(100)  # no error if not found
print("After discard(100) from A:", setA)

# pop()
p = setA.pop()
print("Popped element:", p)
print("After pop():", setA)

# union()
print("Union:", setA.union(setB))

# intersection()
print("Intersection:", setA.intersection(setB))

# difference()
print("Difference (A - B):", setA.difference(setB))

# symmetric difference()
print("Symmetric Difference:", setA.symmetric_difference(setB))

# issubset()
print("Is A subset of B?:", setA.issubset(setB))

# issuperset()
print("Is A superset of B?:", setA.issuperset(setB))

# copy()
copy_set = setA.copy()
print("Copied Set:", copy_set)

# clear()
copy_set.clear()
print("After clear():", copy_set)

output:
# Original List: [10, 20, 30, 40, 20, 50]
# Length: 6
# After append(60): [10, 20, 30, 40, 20, 50, 60]
# After insert(2, 25): [10, 20, 25, 30, 40, 20, 50, 60]
# After remove(20): [10, 25, 30, 40, 20, 50, 60]
# Popped element: 60
# After pop(): [10, 25, 30, 40, 20, 50]
# Index of 30: 2
# Count of 20: 1
# After sort(): [10, 20, 25, 30, 40, 50]
# After reverse(): [50, 40, 30, 25, 20, 10]
# Copied list: [50, 40, 30, 25, 20, 10]
# After clear(): []

# ========== SET FUNCTIONS EXAMPLES ==========
# Set A: {1, 2, 3, 4}
# Set B: {3, 4, 5, 6}
# After add(7) to A: {1, 2, 3, 4, 7}
# After update([8, 9]) to A: {1, 2, 3, 4, 7, 8, 9}
# After remove(2) from A: {1, 3, 4, 7, 8, 9}
# After discard(100) from A: {1, 3, 4, 7, 8, 9}
# Popped element: 1
# After pop(): {3, 4, 7, 8, 9}
# Union: {3, 4, 5, 6, 7, 8, 9}
# Intersection: {3, 4}
# Difference (A - B): {8, 9, 7}
# Symmetric Difference: {5, 6, 7, 8, 9}
# Is A subset of B?: False
# Is A superset of B?: False
# Copied Set: {3, 4, 7, 8, 9}
# After clear(): set()
