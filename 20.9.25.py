# program to check ,each number in a list contains duplicate digits 
# input : [202.89,112,88] 

# def has_duplicates(n):
#     l = str(n)
#     return len(set(l)) != len(l)

# def check_duplicates(num):
#     return [has_duplicates(n) for n in num]

# num = [202,89,112,88]
# print(check_duplicates(num))
# [true,false,true,true]

# 2.sum of all numbers in matrix :
def sum_matrix(n):
    total = 0
    for i in range(len(n)):
        for j in range(len(n[i])):
            total = total + n[i][j]
n = [
    [1,3,5],
    [4,6,8],
    [6,8,4]
]  

print(sum_matrix(n))