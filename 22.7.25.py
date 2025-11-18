#loops
#advantages of loops=>code readability
#for and while
#iterable-list,tuple,range,set,dict,string

# for i in range (0,10):
#     print(i)
#     print('Hello')
#     print('Hi')
# print('Good Morning')

# num1=int(input('enter a number:'))
# for i in range(num1):
#     print(i)

# n=5
# # for i in range(0, n, 2):
# #     print(i)
# for i in range(0,n):
#     if i%2==0:
#         print(i)

#while loop-based on a condition


# i=5
# while i > 3:
#     print('junior cinema ela undhi?')
#     i = i -1


# num1=9
# while num1<10:
#     print(num1)
#     num1-=1

# num1=9
# while num1<10 and num1>=0:
#     print(num1)
#     num1-=1
    

# i=1
# while i <=10:
#     print("17x",i,"=",17*i)
#     i+=1

#string
# n='python'
# for i in n:
#     print(i)

# str1='valli'
# for i in str1:
#     print(i)

# list1=['valli',2,'parveen','3']
# for i in list1:
#     print(i,end=' ')

# set1={23,14,4 ,'prabhas'}
# for i in set1:
#     print(i)

# tuple1=(5,6,7,'parveen')
# for i in tuple1:
#     print(i)

# dict1={
#     1:'parveen',
#     2:'valli',
#     3:'banu',
#     4:'teja'
# }
# for valli in dict1.values():
#     print(valli)

d={10:'valli',20:'parveen'}
for valli in d.items():
    print(valli)