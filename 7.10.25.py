# A
# for i in range(7):
#     for j in range(5):
#         if(j==0 or j==4)and i !=0 or (i==0 or i==3) and (j>0 and j<4):
#             print("*",end="")
#         else:
#             print(" ", end="")
#     print()

# B
# for i in range(7):
#     for j in range(5):
#         if j == 0 or (j==4 and i !=0 and i !=3 and i !=6) or ((i==0 or i==3 or i==6) and j<4):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

#C
# for i in range(7):
#     for j in range(5):
#         if(j==0 and i!=0 and i!=6) or ((i==0 or i==6) and j>0):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

#D
# for i in range(7):
#     for j in range(5):
#         if j == 0 or (j == 4 and i != 0 and i != 6) or ((i == 0 or i == 6) and j < 4):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#E
# for i in range(7):
#       for j in range(5):
#         if j == 0 or i == 0 or i == 3 or i == 6:
#             print("*", end="")
#         else:
#             print(" ", end="")
#       print()

#F
# for i in range(7):
#     for j in range(5):
#         if j == 0 or i == 0 or i == 3:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#G
# for i in range(7):
#     for j in range(5):
#         if (j == 0 and i != 0 and i != 6) or ((i == 0 or i == 6) and j > 0 and j < 4) or (j == 4 and i >= 3) or (i == 3 and j >= 2):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#H
# for i in range(7):
#     for j in range(5):
#         if j == 0 or j == 4 or i == 3:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#I
# for i in range(7):
#     for j in range(5):
#         if i == 0 or i == 6 or j == 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#J
# for i in range(7):
#     for j in range(5):
#         if i == 0 or j == 2 or (i == 6 and j < 2) or (j == 0 and i >= 4):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#K
# for i in range(7):
#     for j in range(5):
#         if j == 0 or i + j == 3 or i - j == 3:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#L
# for i in range(7):
#     for j in range(5):
#         if j == 0 or i == 6:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#M
# for i in range(7):
#     for j in range(7):
#         if j == 0 or j == 6 or (i == j and j < 4) or (i + j == 6 and j > 2):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#N
# for i in range(7):
#     for j in range(7):
#         if j == 0 or j == 6 or i == j:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#O
# for i in range(7):
#     for j in range(5):
#         if (j == 0 or j == 4) and (i != 0 and i != 6) or ((i == 0 or i == 6) and (j > 0 and j < 4)):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#P
# for i in range(7):
#     for j in range(5):
#         if j == 0 or (i == 0 or i == 3) and j < 4 or (j == 4 and i > 0 and i < 3):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#Q
# for i in range(8):
#     for j in range(6):
#         if (j == 0 or j == 4) and (i != 0 and i != 6) or ((i == 0 or i == 6) and (j > 0 and j < 4)) or (i - j == 2 and i > 3):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#R
# for i in range(7):
#     for j in range(5):
#         if j == 0 or (i == 0 or i == 3) and j < 4 or (j == 4 and i > 0 and i < 3) or (i - j == 3):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#S
# for i in range(7):
#     for j in range(5):
#         if (i == 0 or i == 3 or i == 6) and (j > 0 and j < 4) or (j == 0 and (i > 0 and i < 3)) or (j == 4 and (i > 3 and i < 6)):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#T
# for i in range(7):
#     for j in range(5):
#         if i == 0 or j == 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#U
# for i in range(7):
#     for j in range(5):
#         if (j == 0 or j == 4) and i != 6 or (i == 6 and j > 0 and j < 4):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#V
# n = 7  # height of the letter
# for i in range(n):
#     for j in range(2 * n - 1):
#         if j == i or j == (2 * n - 2 - i):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#W
# n = 7  # height of the letter
# for i in range(n):
#     for j in range(7):
#         if j == 0 or j == 6 or (i == j and j > 0 and j < 3) or (i + j == 6 and j > 3 and j < 6):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#X
# n = 7  # height of the letter
# for i in range(n):
#     for j in range(n):
#         if i == j or i + j == n - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#Y
# n = 7  # height of the letter
# for i in range(n):
#     for j in range(n):
#         if (i <= 3 and (i == j or i + j == n - 1)) or (i > 3 and j == n//2):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


#Z
# n = 7  # height of the letter
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or i + j == n - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()








 