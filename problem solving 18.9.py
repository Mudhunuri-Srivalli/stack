# Write time and space complexity for all the P.S codes we have discussed till now.
# Print Factors of a Number
num = 12
for i in range(1, num + 1):
    if num % i == 0:
        print(i)

# Print Even Numbers from 2 to 10 (While Loop)
i = 2
while i <= 10:
    print(i)
    i += 2

# Sum of Numbers from 1 to 5
sum = 0
for i in range(1, 6):
    sum += i
print(sum)

# Check if String is Uppercase
s = "HELLO"
if s.isupper():
    print("UPPERCASE")
else:
    print("lowercase")

# Check Character Upper/Lower
ch = 'A'
if ch.isupper():
    print(ch.lower())
else:
    print("It is already lowercase")

# Find Sum, Max, and Min in List
def find_max_min_sum(list1):
    max_elem = list1[0]
    min_elem = list1[0]
    total = 0

    for i in list1:
        total += i
        if i > max_elem:
            max_elem = i
        if i < min_elem:
            min_elem = i

    print("Sum =", total)
    print("Max =", max_elem)
    print("Min =", min_elem)
