# for i in range(1,101):
# if i%15==15
#     print(i,end="")

# num1=1
# n=15
# fact=1
# while num1<=n:
#     fact=fact*num1
#     num1+=1
#     print(fact)

# def cal_fact(n):
#     if n<0

# password = "admin123"
# attempts = 3
# while attempts > 1:
#     user_input = input("Enter password: ")
#     if user_input == password:
#         print("Login successful")
#         break
#     else:
#         attempts -= 1
#         print(f"Incorrect. {attempts} attempts left.")
# else:
#     print("Account locked")

# num1=12534
# print(len(str(num1)))
# str1=str(num1)
# sum=0
# for i in str1:
#     sum=sum+int(i)
# print(sum)


# print(int(str(num1)[::-1]))


# num1=2456
# count=0
# sum=0
# while num1>0:
#     rem=num1%10
#     print(rem)
#     # que=num1//10
#     # num1=que
#     num1=num1//10
#     count+=1
#     sum+=rem
# print(count)
# print(sum)



# 1. Palindromic Bus Ticket

ticket = input().strip()

# Reverse the ticket number
reverse_ticket = ticket[::-1]

# Check palindrome
if ticket == reverse_ticket:
    print("Lucky Ticket")
else:
    print("Not Lucky")

# intput:
# # 121
# output:
# # Lucky Ticket
# intput:
# 123
# output:
# Not Lucky

# 2. Sum of Magic Squares (Sum of squares 1² + 2² + … + n²)
n = int(input())
total = 0

for i in range(1, n + 1):
    total += i * i

print(total)
 
#  input:
# 3
# output:
# 14
# input:
# 5
# output:
# 55

# 3. Treasure Hunt Guessing Game
secret_number = 42  # you can change this to any number between 1 and 100

while True:
    guess = int(input())
    
    if guess == secret_number:
        print("Treasure Found!")
        break
    else:
        print("Try Again!")
# output:
# Try Again!
# Try Again!
# Treasure Found!

# 4. Perfect Square Festival (1 to 500)
for i in range(1, 501):
    if int(i ** 0.5) ** 2 == i:
        print(i, end=" ")

# output:1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361 400 441 484

# 5. Cube Challenge (Print cubes from 1 to n)

n = int(input())

for i in range(1, n + 1):
    print(i ** 3)

# output:
# 1
# 8
# 27
# 64
# 125



