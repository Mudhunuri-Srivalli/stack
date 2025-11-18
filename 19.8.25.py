# Armstrong Number Program

# Armstrong Number Program

# An Armstrong number (also called Narcissistic number)
# is a number that is equal to the sum of its own digits
# each raised to the power of the number of digits.

num = int(input("Enter a number: "))

# Convert number to string to count digits
digits = str(num)
power = len(digits)

# Calculate Armstrong sum
armstrong_sum = 0
for d in digits:
    armstrong_sum += int(d) ** power

# Check Armstrong condition
if armstrong_sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")

# output:
# 153 is an Armstrong number


