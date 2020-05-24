# t = int(input())
# for a in range(1, t+1):
#     highJ = 0
#     lowJ = 0
#     n = int(input())
#     wall = [0]*51
#     for i in range(1,n+1):
#         wall[i] = int(input())
#         if i != 1:
#             if wall[i] > wall[i-1]:
#                 highJ += 1
#             if wall[i] < wall[i-1]:
#                 lowJ += 1
#     print('Case ', a, ':', highJ, lowJ)

t = int(input())
for a in range(1, t+1):
    highJ = 0
    lowJ = 0
    n = int(input())
    wall = input().split()
    for i in range(n):
        if i != 0:
            if wall[i] > wall[i-1]:
                highJ += 1
            elif wall[i] < wall[i-1]:
                lowJ += 1
    print('Case ', a, ':', highJ, lowJ)