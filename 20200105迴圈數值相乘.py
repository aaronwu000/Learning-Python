a = int(input())
for i in range(1, a+1):
    for j in range(1, a+1):
        if i >= j:
            print('{:4d}'.format(i*j), end="")
    print('\n')
