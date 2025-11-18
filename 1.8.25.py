#functions
# def simple_calculator(a,b):#perameters
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     if b!=0:
#       print(a/b)
#       print(a%b)
#     else:
#        print('division by zero is not possible')    
# simple_calculator(5,6)
# simple_calculator(4,2)#arguments
# simple_calculator(9,4)
# simple_calculator(4,8)
# simple_calculator(14,7)

# def table_print(num1):
#    for i in range(1,21):
#       print(num1,'x',i,'=',num1*i)
# table_print(23)
# table_print(11)
# def n_natural_numbers(n):
#  n=int(input('enter a number:'))
#  sum=0
#  for i in range(1,n+1):
#    sum+=i
#  print(sum)
# n_natural_numbers(8)

def factorial_of_number(n):                                                                                                                      
 n=int(input('enter a number:'))
 sum=1
 for i in range(1,n+1):
   sum*=i
 print(sum)
factorial_of_number(4)


