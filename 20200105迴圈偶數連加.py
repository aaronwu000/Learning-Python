a, b = map(int, input().split())
sum = 0
if a % 2: a += 1
for i in range(a, b+1, 2): sum += i
print(sum)