while True:
    try:
        v, t = map(eval, input().split())
        print(v * t * 2)
    except:
        break