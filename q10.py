
account = 0

while 1:
    print("-"*50)
    print("         1.예금 :: 2.출금 :: 3.잔고 :: 4.종료")
    print("-" * 50)

    c = input("선택: ")

    if c=='1':
        insert = input("예금액: ")
        account += int(insert)
    elif c=='2':
        minus = input("출금액: ")
        account -= int(minus)
    elif c=='3':
        print(account)

    elif c=='4':
        break

    else:
        print("wrong number")
        continue