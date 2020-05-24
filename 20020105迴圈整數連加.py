a, b = map(int, input().split())
sum = 0
"""
while a<=b:
    sum += a
    a+=1
"""
for i in range(a,b+1):
    sum+=i
print(sum)