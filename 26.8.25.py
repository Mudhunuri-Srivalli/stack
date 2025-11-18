#string mtthods
# Accessing string elements
str1="python"
print(str1[0])
print(str1[-1])

# Slicing Strings
str1="python"
print(str1[1:3])
print(str1[:4])
print(str1[3:])
print(str1[:-3])

# Concatenation
str1="Hello"
str2="World"
result=str1+" "+str2
print(result)

# Repetition
str1="hii!"
print(str1*3)

# strip()
text=" Hello World "
print(text.strip())

# lower() 
text="VALLI"
print(text.lower())

# upper
text="valli"
print(text.upper())

# find(substring)
text="Hello,World!"
print(text.find("World!"))

# replace(old, new)
text="I Love Python"
print(text.replace("python","coding"))

# split(delimiter)
text="a,b,c"
print(text.split(","))