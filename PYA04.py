num_list = []
while True:
    a = eval(input())
    if a == 9999:
        break
    num_list.append(a)
# min = num_list[0]
# for i in num_list:
#     if i < min: min = i
print(min(num_list))

