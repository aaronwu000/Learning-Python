while True:
    try:
        id_dict = {'R':25, 'J':18, 'S':26, 'B':11, 'K':19, 'T':27, 'C':12, 'L':20, 'U':28, 'D':13, 'M':21, 'V':29, 'E':14, 'N':22, 'W':32, 'F':15, 'O':35, 'X':30, 'G':16, 'P':23, 'Y':31, 'H':17, 'Q':24, 'Z':33, 'I':34, 'A':10}
        ID = input()
        id_sum = (id_dict[ID[0]] % 10) * 9 + id_dict[ID[0]] // 10
        # for i in range(1, 9):
        #     id_sum += int(ID[i]) * (9 - i)
        mul = 8
        for i in ID[1:9]:
            id_sum += int(i) * mul
            mul -= 1
        id_sum += int(ID[9])
        print('real' if id_sum % 10 == 0 else 'fake')
    except:
        break
