# n=input('enter str:')
# for i in n:
#     if'A'<= i<='z':
#         res=chr(ord(i)+32)
#         print(res)
#     else:
#         print('already lower case')


# l=[24,12,26,9,7,5]
# for i in l:
#     if i%2==0:
#        print(i)
# else:
#        print('odd')

# for roll_no in range(1,31):
#      print('class 1','roll',roll_no)
# for roll_no in range(1,31):
#      print('class 2','roll',roll_no)
# for roll_no in range(1,31):
#      print('class 3','roll',roll_no)
# for roll_no in range(1,31):
#      print('class 4','roll',roll_no)
count=0
for class_no in range(1,5):
#      print(class_no)
     for roll_no in range(1,15):
         count+=1
         print('class ',class_no,'roll',roll_no)
print(count)





