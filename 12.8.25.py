
# method 1
num1=int(input('enter a number'))
count=0
for i in range(1,num1+1):
    if num1%i==0:
        count+=1
if count==2:
        print('prime number')
else:
        print('not a prime number')
# method 2
if num1<=1:
      print('not a prime number')
else:
      flag=True
      for i in range(2,num1):
          if num1%i==0:
              flag=False
              print('not a prime number')
              break
      if flag:
            print('prime')




def check_even(num1):
      if num1%2==0:
            return True
      else:
            return False
      
def check_even(num1):
      if num1%2==0:
            return True
      
            return False
      


def check_prime(in_num):
      if in_num<=1:
            return'not a prime'
      for i in range(2,in_num):
            if in_num%i==0:
                  return'not a prime'
                  
      return 'prime'

#method 3
def check_prime(in_num):
      if in_num<=1:
            return'not a prime'
      for i in range(2,in_num//2+1):
            if in_num%i==0:
                  return'not a prime'
                  
      return 'prime'
print(check_prime(23)) 