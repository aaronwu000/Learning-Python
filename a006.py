while True:
    try:
        a, b, c = map(int, input().split())
        D = b ** 2 - 4 * a * c
        if D > 0:
            x1 = int((-b + D ** 0.5) / (a * 2))
            x2 = int((-b - D ** 0.5) / (a * 2))
            print("Two different roots x1=" + str(x1) + " , x2=" + str(x2))
        elif D == 0:
            x = int(-b / (a * 2))
            print("Two same roots x=" + str(x))
        else:
            print("No real root")
    except:
        break
