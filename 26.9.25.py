# Print first n natural numbers using recursion.

# N natural numbers using recursion in reverse order

# First n even numbers using recursion


# 1. Print first n natural numbers using recursion
def print_natural(n):
    if n > 0:
        print_natural(n-1)   # recursive call
        print(n, end=" ")

# 2. Print n natural numbers in reverse order using recursion
def print_reverse(n):
    if n > 0:
        print(n, end=" ")
        print_reverse(n-1)

# 3. Print first n even numbers using recursion
def print_even(n):
    if n > 0:
        print_even(n-1)
        print(2*n, end=" ")

# Driver code
n = 10
print("First", n, "natural numbers:")
print_natural(n)

print("\n\nFirst", n, "natural numbers in reverse order:")
print_reverse(n)

print("\n\nFirst", n, "even numbers:")
print_even(n)


# ouy put:
# First 10 natural numbers:
1 2 3 4 5 6 7 8 9 10 

First 10 natural numbers in reverse order:
10 9 8 7 6 5 4 3 2 1 

First 10 even numbers:
2 4 6 8 10 12 14 16 18 20
