#reverse a list
# list1=[10,20,50,-32,67]
# #method-1
# list1.reverse() 
# print(list1)
#method-2
# print(list1[:: -1])
# list1=list1[:: -1]
# print(list1)


# new_list=[]
# for i in list1:
#     new_list.insert(0,i)

# print(new_list)
# list1=new_list
# print(new_list)
 
# list1=[10,20,50,-32,67]
# for ind in range(0,len(list1)):
#     print(ind)
#     print(list1[ind])

# list1=[10,20,50,-32,67]
# for ind in range(len(list1)-1,-1,-1):
#     print(ind)
#     print(list1[ind])

# list1=[10,20,50,-32,67]
# new_list=[]
# for i in list1:
#     new_list.append(i,0)

#efficient approach




list1=[10,20,50,-32,67]
low=0
high=(len(list1)-1)
while low<high:
    list1[low],list1[high]=list1[high],list1[low]
    low+=1
    high-=1
print(list1)


list1=[10,20,50,-32,67]
low=0
high=(len(list1)-1)//2
while low<high:
    list1[low],list1[high]=list1[high],list1[low]
    low+=1
    high-=1
print(list1)



#reverse the string by using above code
#[123,345,61,3,45] num sum of dig of each number in give list.out put shoud be in the give list
#find max digit in the given number
#find max digit for every number in the given list



#tommorow class
#sorting alogithem 
#searching alogithem
#bubble sort
#linear search
#binary search