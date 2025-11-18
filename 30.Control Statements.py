# 1. Check Even or Odd
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# 2. Find the Greatest of Two Numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     print("First number is greater")
# elif b > a:
#     print("Second number is greater")
# else:
#     print("Both are equal")

# # 3. Find the Greatest of Three Numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a >= b and a >= c:
#     print("First number is greatest")
# elif b >= a and b >= c:
#     print("Second number is greatest")
# else:
#     print("Third number is greatest")

# # 4. Positive, Negative, or Zero
# num = float(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# # 5. Sum of First N Natural Num
# n = int(input("Enter a number: "))
# total = 0
# for i in range(1, n + 1):
#     total += i
# print("Sum is", total)

# # 6. Print Even Numbers from 1 to N
# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         print(i)

# # 7. Table of a Number
# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

# # 8. Count from 1 to 10 Using While Loop
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# # 9. Sum of Digits
# num = int(input("Enter a number: "))
# sum_digits = 0
# while num > 0:
#     sum_digits += num % 10
#     num //= 10
# print("Sum of digits:", sum_digits)

# # 10. Simple Login System
# password = "admin123"
# attempts = 3
# while attempts > 0:
#     user_input = input("Enter password: ")
#     if user_input == password:
#         print("Login successful")
#         break
#     else:
#         attempts -= 1
#         print(f"Incorrect. {attempts} attempts left.")
# else:
#     print("Account locked")

# # 11. Skip Multiples of 3
# for i in range(1, 21):
#     if i % 3 == 0:
#         continue
#     print(i)

# # 12. Break on Input Zero
# while True:
#     num = int(input("Enter a number (0 to stop): "))
#     if num == 0:
#         break
#     print(f"You entered: {num}")

# # 13. Count Even and Odd in a List of 5 Numbers
# even = 0
# odd = 0
# for i in range(5):
#     num = int(input(f"Enter number {i+1}: "))
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Even numbers:", even)
# print("Odd numbers:", odd)

# # 14. Print All Characters in a Word
# word = input("Enter a word: ")
# for char in word:
#     print(char)

# # 15. Check Divisibility
num = int(input("Enter a number: "))
if num % 2 == 0 and num % 5 == 0: 
    print("Divisible by both 2 and 5")
else:
    print("Not divisible by both")

