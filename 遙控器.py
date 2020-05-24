while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    if a > b:
        a, b = b, a
    print(min(b - a, 100 - b + a))
