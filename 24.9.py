# sum of two leargest numbers
a=55
b=2
c=98
if a>b and a>c:
    if b>c:
     print(a+b)
    else:
        print(a+c)
elif b>a and b>c:
    if a>c:
       print(a+b)
    else:
       print(b+c)
else:
    if a>b:
       print(c+a)
    else:
       print(c+b)


# rotation of a matrix
m=[[1,2,3],
  [4,5,6],
  [7,8,9]]
for i in range(len(m)):
   for j in range(len(m)-1,-1,-1):
      print(m[j][i],end=" ")
   print()
# [importent***********
# integer_1=int(input())
# float=float(input())
# string=input()
# a,b,c=map(int,input().split())
# list=list(map(int,input().split()))
# n=int(input())
# matrix=[]
# for i in range(n):
#     l=list(map(int,input().split()))
#     matrix.append(l)
# ***************************]


# integer_1=int(input())

# a,b,c=map(int,input("enter").split())
# print(a+b+c)

# float=float(input())

#   list=list(map(int,input("enter elements").split))
