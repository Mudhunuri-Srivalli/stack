#jump statement
# for i in range(1,20):
#     print(i)
#     if i==5:
#         break
#     print(i)

# for i in range(1,20):
#     if i<5:
#         print(i)
#         print(i)
#     elif i ==5:
#         print(i)

# for i in range(1,31):
#    print(i*2567)
#    break
#    print(i*2567)

# for i in range(0,31):
#     if i<i*(-1)or i%5==0:
#         break
#     print(i**2)

#continue
# for i in range (1,34):
#     print(i)
#     print(i)
#     if i==6 or i==7:
#         continue
#     print(i)

# for i in range(1,45):
#     continue
#     print(i)

# i=5
# while i<25:
#     print(i)
#     i-=1

#     if i % 5 == 0:
#        break


#for 
# for class_no in range(1,11):
#     if class_no==4:
#           continue
#     for roll_no in range(1,31):
#            if roll_no==5:
#                 continue
#            print('class1',class_no, "roll",roll_no)


#pass

# num1=10

# if num1 % 2==0:
#      pass
# else:
#       print('number is odd')



for class_no in range(1,11):
      for roll_no in range(1,31):
            if class_no%5==0 or roll_no<15:
                  break
            print('class1',class_no, "roll",roll_no)
      
for class_no in range(1,11):
      for roll_no in range(1,31):
            if class_no%5==0 or roll_no>15:
                  break
            print('class1',class_no, "roll",roll_no)
      



