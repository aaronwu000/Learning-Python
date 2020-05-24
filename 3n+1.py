# try:
#     while True:
#         i, j = map(int, input().split())
#         iOri=i
#         jOri=j
#         if i > j:
#             i, j = j, i
#         maxNum = 0
#         for n in range(i, j + 1):
#             count = 0
#             while True:
#                 # print(n, end=' ')
#                 count += 1
#                 if n == 1:
#                     break
#                 if n % 2 == 1:
#                     n = 3 * n + 1
#                 else:
#                     n = n / 2
#             if count > maxNum:
#                 maxNum = count
#         print(iOri, ' ', jOri, ' ', maxNum)
# except:
#     pass
while True:
    try:
        while True:
            i, j = map(int, input().split())
            maxNum = 0
            for n in range(min(i, j), max(i, j) + 1):
                count = 0
                while True:
                    # print(n, end=' ')
                    count += 1
                    if n == 1:
                        break
                    if n % 2 == 1:
                        n = 3 * n + 1
                    else:
                        n = n / 2
                if count > maxNum:
                    maxNum = count
            print(i, ' ', j, ' ', maxNum)
    except:
        break
