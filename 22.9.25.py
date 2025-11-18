# def sock_days(socks):
#     sock_counts = {}
#     for color in socks :
#         if color in sock_counts:
#             sock_counts[color] += 1
#         else:
#             sock_counts[color] = 1


#     total_pairs = 0
#     for count in sock_counts.values():
#         total_pairs += count //2

#     return total_pairs    
# socks = ['red', 'green', 'red', 'purple', 'green', 'black', 'red']
# print(sock_days(socks)) #2 


# Find the Missing Numbers
# nums = '34571'
# present = set(nums)
# all_digits = set('0123456789')

# missing = sorted(all_digits - present)
# print("Missing digits:", ''.join(missing))
# print("Total missing:", len(missing))
# output:
# Missing digits: 02689
# Total missing: 5

# 3.Matrix addition using range.

# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

# B = [[9, 8, 7],
#      [6, 5, 4],
#      [3, 2, 1]]

# rows = len(A)
# cols = len(A[0])

# result = []
# for i in range(rows):
#     row = []
#     for j in range(cols):
#         row.append(A[i][j] + B[i][j])
#     result.append(row)

# print("Matrix Addition Result:")
# for r in result:
#     print(r)
# Matrix Addition Result:
# [10, 10, 10]
# [10, 10, 10]
# [10, 10, 10]
