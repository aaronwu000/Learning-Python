n, m = map(int, input().split())
score = [0]*(n+1)
for i in range(1, n+1):
    score[i] = int(input())
for i in range(m):
    search = int(input())
    print(score[search])