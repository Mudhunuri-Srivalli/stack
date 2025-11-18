# 1.Print list in a reverse order 
# 2.Print exponent of two numbers without using double star operator & loops


# 1. Print list in reverse order

# Method 1 – Using slicing:

my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)
print("Reversed List:", my_list[::-1])


# Method 2 – Using reversed():

my_list = [1, 2, 3, 4, 5]
print("Reversed List:", list(reversed(my_list)))


# Method 3 – Without built-in functions (manual indexing):

my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)-1, -1, -1):
    print(my_list[i], end=" ")

# 2. Print exponent of two numbers (without ** operator & without loops)

# We can use recursion:

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

# Example
x = 2
y = 5
print(f"{x}^{y} =", power(x, y))


# Output:

2^5 = 32