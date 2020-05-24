sec = int(input())
hour = sec // 3600
min = (sec % 3600) // 60
sec = sec%60
print(str(hour), ' hr ', str(min), ' min ', str(sec), ' sec ')