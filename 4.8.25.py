# def connect_to_db(*args):
#     print(args)
# connect_to_db('localhost:300','2345','3300','2243')




# def connect_to_db2(**kargs):
#     print(kargs)
#     print(type(kargs))
# connect_to_db2(db_loc='localhost:300',db_pool='2345',db_port='3300',db_password='2243') 




# def add (num1,num2):
#     print(num1+num2)
# add(2,5)



# def add2 (num1,num2):
#     return num1+num2
# result=add2(2,5)
# print(add2(4,5))
# print(result)
# print(result*5)
 #return statement once executed is the function call gets end

def even_or_odd(num1):
    if num1%2==0:
        return 'even'
    else:
        return 'odd'
    r1=even_or_odd(25)
    print(r1)


def  simple_calculator(a,b):
    return a+b,a-b,a*b


r2=simple_calculator(2,5)
print(r2)
print(type(r2))


def even_or_odd(num1):
    if num1%2==0:
        return 'even'
    else:
        return 'odd'
    
    print('na sav nen sastha niku endhuku')
r1=even_or_odd(22)
r2=even_or_odd(23)

