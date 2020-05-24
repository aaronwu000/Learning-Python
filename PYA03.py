a = eval(input())
b = eval(input())
total = 0
a += 1 if a % 2 != 0 else 0
for i in range(a, b+1, 2): total += i
print(total)


