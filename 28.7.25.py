# for i in range(1,21):
#      print(f"1x{i}={1*i}")
# for i in range(1,21):
#      print(f"2x{i}={2*i}")
# for i in range(1,21):
#      print(f"3x{i}={3*i}")
# for i in range(1,21):
#      print(f"4x{i}={4*i}")
# for i in range(1,21):
#      print(f"5x{i}={5*i}")
# for i in range(1,21):
#      print(f"6x{i}={6*i}")

# for j in range(1,10):
#      for i in range(1,21):
#           print(j,'x',i,'=',j*i)
# count=0
# for class_no in range(1,11):
#     print(class_no)
#     for roll_no in range(1,31):
#         if roll_no%2==0:
#             print('class1',class_no,'roll','roll_no')
#             count+=1
# print(count)

# for class_no in range(1,11):
#      if class_no%2==0:
#         for roll_no in range(1,31):
#            print('class1',class_no, "roll",roll_no)
            


class_no = 1
while class_no <= 10:
    if class_no % 2 == 0:
        roll_no = 1
        while roll_no <= 30:
            print('class1', class_no, "roll", roll_no)
            roll_no += 1 
    class_no += 1


class_no = 1
while class_no < 11:
    roll_no=1
    while roll_no<31:
        print('class1', class_no, "roll", roll_no)
        roll_no += 1 
    class_no += 1
