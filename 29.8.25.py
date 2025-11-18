#reversing a number 
# num1=int(input("enter a number:"))
# rev_num=0
# while num1>0:
#     digit=num1%10
#     rev_num=rev_num*10+digit
#     print(digit)
#     num1=num1//10
#     print(rev_num)

#print even digits
#print prime digits in a given number
#if rev_num==temp pallindrome


#swapping
num1=10
num2=20
#method 1
# num1,num2=num2,num1


#method 2
temp=num2
num2=num1
num1=temp
print(num1,num2)



#method 3
num1=10
num2=20

num1=num1+num2
num2=num1-num2
num1=num1-num2


#method 4-XOR properties
# 1 property=>
# x=5
# print(x^x)  op:0
# print(x^0) op:5

num1=10
num2=20
num1=num1^num2 #(10^20)
num2=num1^num2 #(10^20)^20 #10^0 #10
num1=num1^num2 #(10^20)^10 #0^20 #20







#petfect number
# 6=>1,2,3=>6
#6=>sum(1,2,3)=>6