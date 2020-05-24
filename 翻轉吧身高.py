# 輸入說明
#
# 第1列：一個整數N，代表班上同學有N位。N <= 100
#
# 接著N列：同學的身高（座號順序顛倒）。
# 輸出說明
#
# 共N列：同學的身高（座號順序正確）。
height = []
n = int(input())
for i in range(n):
    height.append(int(input()))
# for i in range(9,-1,-1):
#     print(height[i])


#陣列反轉
#方法一
# height.reverse()
# print(height)

#方法二
# height = reversed(height)
# print(height)

#方法三
print(height[::-1])