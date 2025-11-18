# Height of letters
# n = 7

# for i in range(n):
#     # Letter V
#     for j in range(2*n-1):
#         if j == i or j == 2*n-2-i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("  ", end="")  # space between letters

#     # Letter A
#     for j in range(5):
#         if (j == 0 or j == 4) and i != 0 or (i == 0 or i == 3) and (j > 0 and j < 4):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("  ", end="")

#     # Letter M
#     for j in range(7):
#         if j == 0 or j == 6 or (i == j and j < 4) or (i + j == 6 and j > 2):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("  ", end="")

#     # Letter S
#     for j in range(5):
#         if (i == 0 or i == 3 or i == 6) and (j > 0 and j < 4) or (j == 0 and i > 0 and i < 3) or (j == 4 and i > 3 and i < 6):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("  ", end="")

#     # Letter I
#     for j in range(5):
#         if i == 0 or i == 6 or j == 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()  # move to next line




# Height of letters
# n = 7

# for i in range(n):
#     # Letter S
#     for j in range(5):
#         if (i == 0 or i == 3 or i == 6) and (j > 0 and j < 4) or (j == 0 and i > 0 and i < 3) or (j == 4 and i > 3 and i < 6):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("  ", end="")

#     # Letter A
#     for j in range(5):
#         if (j == 0 or j == 4) and i != 0 or (i == 0 or i == 3) and (j > 0 and j < 4):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("  ", end="")

#     # Letter H
#     for j in range(5):
#         if j == 0 or j == 4 or i == 3:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("  ", end="")

#     # Letter I
#     for j in range(5):
#         if i == 0 or i == 6 or j == 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("  ", end="")

#     # Letter T
#     for j in range(5):
#         if i == 0 or j == 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("  ", end="")

#     # Letter H
#     for j in range(5):
#         if j == 0 or j == 4 or i == 3:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("  ", end="")

#     # Letter I
#     for j in range(5):
#         if i == 0 or i == 6 or j == 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()  # move to next line



# Height of letters
n = 7

for i in range(n):
    # Letter V
    for j in range(2*n-1):
        if j == i or j == 2*n-2-i:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # Letter A
    for j in range(5):
        if (j == 0 or j == 4) and i != 0 or (i == 0 or i == 3) and (j > 0 and j < 4):
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # Letter L
    for j in range(5):
        if j == 0 or i == 6:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # Letter L (again)
    for j in range(5):
        if j == 0 or i == 6:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # Letter I
    for j in range(5):
        if i == 0 or i == 6 or j == 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # move to next line

