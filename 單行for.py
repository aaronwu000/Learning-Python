# num_list = [0]*50


# num_list = []
# for i in range(1, 51):
#     num_list.append(i)
# num_list = [i for i in range(1, 51)]
# print(num_list)

num_list = [i for i in range(1, 51) if i % 2 == 0]
print(num_list)