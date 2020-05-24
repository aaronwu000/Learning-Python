seq = 0
while True:
    try:
        n, m, c = map(int, input().split())
        if n == m == c == 0:
            break
        seq += 1
        n_amperes = [0]*21
        n_switch = [0]*21
        total = 0
        maxTotal = 0
        s = 'Fuse was not blown.'
        for i in range(1, n + 1):
            n_amperes[i] = int(input())
        for i in range(1, m + 1):
            oper = int(input())
            if n_switch[oper] == 0:
                n_switch[oper] = 1
                total += n_amperes[oper]
                if total > maxTotal:
                    maxTotal = total
                if total > c:
                    s = 'Fuse was blown.'
            else:
                n_switch[oper] = 0
                total -= n_amperes[oper]
        print('Sequence ', seq)
        print(s)
        if s == 'Fuse was not blown.':
            print('Maximal power consumption was ', maxTotal, ' amperes.')
        print()
    except:
        break