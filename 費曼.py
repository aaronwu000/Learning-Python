while True:
    num = int(input())
    sum = 0
    if num == 0:
        break
    for i in range(1, num+1):
        sum += i**2
    print(sum)