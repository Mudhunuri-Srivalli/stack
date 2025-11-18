# Print factors of a numbe
num = 12
print("Factors of", num, ":")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)

# Print even numbers from 2 to 10 using while loop
i = 2
while i <= 10:
    print(i)
    i += 2


# Sum of numbers from 1 to 5
sum = 0
for i in range(1, 6):
    sum += i
print("Sum =", sum)

# Check if a string is uppercase or not
s = "HELLO"
if s.isupper():
    print("String is in UPPERCASE")
else:
    print("String is in lowercase")

# Check if a single character is uppercase or not
ch = 'A'
if ch.isupper():
    print(ch.lower())  # convert to lowercase
else:
    print("It is already lowercase")
