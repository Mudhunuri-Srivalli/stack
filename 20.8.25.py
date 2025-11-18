# Prime number in given range and Armstrong number in range 
# Program: Prime Numbers and Armstrong Numbers in a Range

# ------------------------------
# Function to check Prime Number
# ------------------------------
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# ------------------------------------
# Function to check Armstrong Number
# ------------------------------------
def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** power
    return total == num

# ------------------------------------
# MAIN PROGRAM
# ------------------------------------
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"\nPrime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")

print(f"\n\nArmstrong numbers between {start} and {end}:")
for num in range(start, end + 1):
    if is_armstrong(num):
        print(num, end=" ")


# output:
# Prime numbers between 1 and 500:
# 2 3 5 7 11 13 17 ... 499

# Armstrong numbers between 1 and 500:
# 1 153 370 371 407
