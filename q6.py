
while 1:
    a= input("숫자를 입력하세요: ")
    print(type(a))
    print(a.isdigit())
    if a.isdigit()==True:

     if int(a)%2==0:
                print("evens")
     elif int(a)%2!=0:
                print("odds")

    elif type(a)!=int:
        print("숫자가 아닙니다.")

    elif a=="q":
        break

