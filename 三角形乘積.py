a=int(input())

for i in range(1,a+1,):
    print("{:<8d}".format(i))
    for j in range(1,a+1):
        print(j)