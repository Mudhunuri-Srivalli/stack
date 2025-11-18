#pattren program 
n=5
for i in range(1,n+1):
    print("*"*i)
#reverse print
n=5
for i in range(n,0,-1):
    print("*"*i)
#right triangle
row=5
for i in range(1,n+1):
    print(" "*(n-1)+"*"*i)
#Pyramid 
row=5
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
#Diamond
n=5
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))
#Number
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
       print(j, end=" ")
    print()

