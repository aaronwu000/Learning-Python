import sys

users = [[1090001, 'Mike', '111111', 6000000],
         [1090002, 'Peter', '222222', 500]]

ID = -1


def check(s: str):
    if s.isdecimal():
        return True
    return False


def passwordCheck(p: str):
    if not p.isdecimal() or len(p) != 6:
        return False
    return True


def login():
    account = input('請輸入您的賬戶：')
    if not account.isdecimal() or len(account) < 7:
        print('\n輸入不合法，自動返回...')
        return
    else:
        account = int(account)
    password = input('請輸入使用者密碼：')
    if not passwordCheck(password):
        print('\n輸入不合法，自動返回...')
        return
    for i in range(len(users)):
        if users[i][0] == account and users[i][2] == password:
            print('登入成功！')
            global ID
            ID = i
            break
    if ID == -1:
        print('\n賬戶不存在或密碼錯誤！ 自動返回...')
    else:
        fun()


def register():
    username = input('請輸入使用者名稱：')
    if username == '':
        print('\n輸入不合法，自動返回...')
        return
    password = input('請輸入使用者密碼(密碼為6位數字組成)：')
    if not passwordCheck(password):
        print('\n輸入不合法，自動返回...')
        return
    m = 0
    for i in users:
        m = max(m, i[0])
    users.append([m + 1, username, password, 0])
    print('\n註冊成功！ 您的賬戶為：', m + 1)


def main():
    while True:
        print('\n\n      ******************')
        print('       *自動提款機系統*')
        print('      ******************\n')
        print('*********************************')
        print('******   登入-------1  **********')
        print('******   註冊-------2  **********')
        print('******   退出-------0  **********')
        print('*********************************\n')
        v = input('請輸入對應的數字：')
        if not check(v) or 2 < int(v) or int(v) < 0:
            print('\n輸入不合法，請重新輸入！')
            continue
        else:
            v = int(v)
        if v == 2:
            register()
        elif v == 1:
            login()
        elif v == 0:
            sys.exit(0)


def fun():
    while True:
        print('\n***************************************')
        print('********  查詢--------1  **********')
        print('********  取款--------2  **********')
        print('********  存款--------3  **********')
        print('********  轉賬--------4  **********')
        print('********  修改密碼----5  **********')
        print('********  返回上一層------6  **********')
        print('********  退出------------0  **********')
        print('***************************************\n')
        v = input('請輸入對應的數字：\n')
        if not check(v) or 6 < int(v) or int(v) < 0:
            print('\n輸入不合法，請重新輸入！')
            continue
        else:
            v = int(v)

        if v == 1:
            print('您的當前餘額為：', users[ID][3])
        elif v == 2:
            money = input('請輸入取款金額：')
            if not check(money):
                print('\n輸入不合法，自動返回...')
                continue
            else:
                money = int(money)
            if money > users[ID][3]:
                print('餘額不足，不能取款')
            else:
                users[ID][3] -= money
                print('\n取款成功！ 您的餘額還有', users[ID][3], '元')
        elif v == 3:
            money = input('請輸入存款金額：')
            if not check(money):
                print('\n輸入不合法，自動返回...')
                continue
            else:
                money = int(money)
            users[ID][3] += money
            print('\n存款成功！ 您的餘額還有', users[ID][3], '元')
        elif v == 4:
            anotherID = -1
            account = input('請輸入對方賬戶：')
            if not check(account):
                print('\n輸入不合法，自動返回...')
                continue
            else:
                account = int(account)
            for i in range(len(users)):
                if users[i][0] == account:
                    anotherID = i
                    break
            if anotherID == -1:
                print('\n該賬戶不存在，自動返回...')
                continue
            money = input('請輸入轉賬金額：')
            if not check(money):
                print('\n輸入不合法，自動返回...')
                continue
            else:
                money = int(money)
            if money > users[ID][3]:
                print('餘額不足，轉賬失敗,自動返回...')
                continue
            else:
                users[ID][3] -= money
                users[anotherID][3] += money
                print('轉款成功！ 您的餘額還有', users[ID][3], '元')

        elif v == 5:
            password = input('請輸入舊密碼：')
            if password == users[ID][2]:
                password1 = input('請輸入使用者密碼(密碼為6位數字組成)：')
                if not passwordCheck(password1):
                    print('\n密碼輸入非法，自動返回...')
                    continue
                password2 = input('請再次輸入密碼：')
                if password1 != password2:
                    print('兩次密碼輸入不一致，請重新輸入：')
                else:
                    users[ID][2] = password2
                    print('密碼修改成功！')
            else:
                print('\n密碼輸入錯誤，自動返回...')
        elif v == 0:
            sys.exit(0)
        elif v == 6:
            main()


main()
