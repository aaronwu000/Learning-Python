N = int(input())
T = int(input())
data = [0]*N
for i in range(T):
    n, t, change = map(int, input().split())
    if t == 1:
        data[n] += change
    elif t == 2:
        data[n] -= change
for i in range(N):
    print(i, ' : ', data[i])