                                                                                                                       # 1. Square Hollow Pattern
def square_hollow(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# 2. Number Triangular
def number_triangular(n):
    for i in range(1, n+1):
        print((str(i)+" ")*i)

# 3. Number Increasing Pyramid
def number_increasing_pyramid(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

# 4. Number Increasing Reverse Pyramid
def number_increasing_reverse(n):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

# 5. Number Changing Pyramid
def number_changing_pyramid(n):
    num = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(num, end=" ")
            num += 1
        print()

# 6. Zero-One Triangle
def zero_one_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print((i+j) % 2, end=" ")
        print()

# 7. Palindrome Triangle
def palindrome_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
        for j in range(i-1, 0, -1):
            print(j, end="")
        print()

# 8. Rhombus Pattern
def rhombus(n):
    for i in range(n):
        print(" " * (n-i-1) + "* " * n)

# 9. Diamond Pattern
def diamond(n):
    for i in range(n):
        print(" "*(n-i-1) + "* "*(i+1))
    for i in range(n-2, -1, -1):
        print(" "*(n-i-1) + "* "*(i+1))

# 10. Butterfly Star Pattern
def butterfly(n):
    for i in range(1, n+1):
        print("*"*i + " "*(2*(n-i)) + "*"*i)
    for i in range(n, 0, -1):
        print("*"*i + " "*(2*(n-i)) + "*"*i)

# 11. Square Fill Pattern
def square_fill(n):
    for i in range(n):
        print("* "*n)

# 12. Right Half Pyramid
def right_half_pyramid(n):
    for i in range(1, n+1):
        print("*"*i)

# 13. Reverse Right Half Pyramid
def reverse_right_half(n):
    for i in range(n, 0, -1):
        print("*"*i)

# 14. Left Half Pyramid
def left_half_pyramid(n):
    for i in range(1, n+1):
        print(" "*(n-i) + "*"*i)

# 15. Reverse Left Half Pyramid
def reverse_left_half(n):
    for i in range(n, 0, -1):
        print(" "*(n-i) + "*"*i)

# 16. K Pattern
def k_pattern(n):
    for i in range(n, 0, -1):
        print("*"*i)
    for i in range(2, n+1):
        print("*"*i)

# 17. Triangle Star Pattern
def triangle_star(n):
    for i in range(1, n+1):
        print(" "*(n-i) + "* "*(i))

# 18. Reverse Number Triangle
def reverse_number_triangle(n):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

# 19. Mirror Image Triangle
def mirror_triangle(n):
    for i in range(1, n+1):
        print(" "*(n-i), end="")
        for j in range(1, i+1):
            print(j, end="")
        print()

# 20. Hollow Triangle Pattern
def hollow_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            if j==1 or j==i or i==n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# 21. Hollow Reverse Triangle
def hollow_reverse_triangle(n):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            if j==1 or j==i or i==n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# 22. Hollow Diamond
def hollow_diamond(n):
    for i in range(1, n+1):
        print(" "*(n-i), end="")
        for j in range(1, 2*i):
            if j==1 or j==2*i-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    for i in range(n-1, 0, -1):
        print(" "*(n-i), end="")
        for j in range(1, 2*i):
            if j==1 or j==2*i-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# 23. Hollow Hourglass
def hollow_hourglass(n):
    for i in range(n, 0, -1):
        print(" "*(n-i), end="")
        for j in range(1, 2*i):
            if j==1 or j==2*i-1 or i==n:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    for i in range(2, n+1):
        print(" "*(n-i), end="")
        for j in range(1, 2*i):
            if j==1 or j==2*i-1 or i==n:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# 24. Pascal’s Triangle
def pascal(n):
    for i in range(n):
        print(" "*(n-i), end="")
        num = 1
        for j in range(i+1):
            print(num, end=" ")
            num = num*(i-j)//(j+1)
        print()

# 25. Right Pascal’s Triangle
def right_pascal(n):
    for i in range(1, n+1):
        print("*"*i)
    for i in range(n-1, 0, -1):
        print("*"*i)


      