# print 6th index
# def sixth_element(list1):
#     i = 0
#     for item in list1:
#         if i == 6:
#             print(item)
#             return
#         i += 1
#     print("index out  of range")    
# list1 = [1,2,3,4,5,9,-32,-45]
# print(sixth_element(list1))
# index
# def find_element(input_list,input_index):
#     if input_index < -len(input_list) or input_index >= len(input_list):
#         return "invalid index"
#     return input_list[input_index]
    
# index = int(input("enter index:"))
# list1 = [1,2,3,4,5,9,-32,-45]
# print(find_element(list1,index))

# sum 
# def list_sum(list1):
#    s=0
#    for item in list1:
#        s = s + item 
#    return s

# list1 = [1,2,3,4,5,6,7,8]  
# print(list_sum(list1))

# max in a list

# def find_max(list1):
#     maximum = list1[0]
#     for item in list1:
#         if item > maximum:
#             maximum = item 
#     return maximum

# list1 = [1,3,5,7,9,0]
# print(find_max(list1))   
# 
# min in a list

# def find_min(list1):
#     minimum = list1[0]
#     for item in list1:
#         if item < minimum:    
#             minimum = item
#     return minimum
# list1 = [1,3,5,7,9,0]
# print(find_min(list1))

# def reverse(list1):
    
# list1=[10,20,50,-32,67]
# list1=list1[: : -1]
# print(list1) method 1
# method 2
# list1.reverse()
# print(list1) 

# new_list = []
# for i in list1:
#     new_list.insert(0,i)

# print(list1)
# print(new_list)   


# list1=[10,20,50,-32,67]
# for ind in range(len(list1)-1):
#     print(ind)
#     print(list1[ind])
# print all elements in evn index &also elemnts
# to add elements jst like the previous list we use append  
# list1 = [10,20,50,-32,67]
# new_list = []
# for i in list1:
#     new_list.append(i)

# print(list1)
# print(new_list) 

# list1 = [10,20,30,5,72,91,0]
# n = len(list1)
# for i in range(n//2):
#     list1[i],list1[n-i-1]=list1[n-i-1],list1[i]

# print(list1)

# reverse a string using alll the approaches 
# find max of 123 
# [123,345,61,3,45] sum of particular index 
# find max digit for every number in the given list 


# def reverse_string(str1):
#     rev = ""
#     for i in range(len(str1) - 1, -1, -1):
#         rev += str1[i]
#     return rev

# print(reverse_string("python"))

# lst= [10,20,30,40]
# # list[: : -1]
# print(list(reversed(lst)))

# numbers=[2,4,6,8]
# reversed_number=numbers.reverse()
# print(reversed_number)

# using while loop 

# def reverse_string(str1):
#     rev = ""
#     i = len(str1)-1
#     while i >= 0:
#         rev += str1[i]
#         i -= 1
#     return rev 

# print(reverse_string("world"))   

# to use two-pointer method we need to convert it to list 

# def reverse_string(s):
#     chars = [c for c in s]  
#     left, right = 0, len(chars) - 1
#     while left < right:
#         chars[left], chars[right] = chars[right], chars[left]
#         left += 1
#         right -= 1
#     rev = ""
#     for c in chars:
#         rev += c
#     return rev

# print(reverse_string("reverse"))


# Sum of digits of each number in the given list. Output should be in list format

# def sum_digits_list(list1):
#     result = []
#     for num in list1:
#         sum=0
#         n=num
#         while n > 0:
#             digit = n % 10
#             sum += digit
#             n //= 10
#         result.append(sum)
#     return result
# list1=[123,45,67,890]
# print(sum_digits_list(list1))  #[6,9,13,17]
      

# find max digit in the given number:

# def find_max_digit(num):
#     max_d = 0
#     n = num
#     while n > 0:
#         digit = n % 10 
#         if digit > max_d:    
#          max_d = digit
#         n //= 10             
#     return max_d


# print(find_max_digit(21052004))


# ind max digit for every number in the given list

def max_digit_each(lst):
    result = []
    for num in lst:
        n = num
        max_d = 0
        while n > 0:
            digit = n % 10
            if digit == 9:   
                max_d = 9
                break
            if digit > max_d:
                max_d = digit
            n //= 10
        result.append(max_d)
    return result
numbers = [123, 4567, 890, 9325]
print(max_digit_each(numbers))

