
a=input("숫자를 입력하세요: ")
a=int(a)

if a%2==0:
    s = 0
    for a in range(0,a+1,2):
        s +=a
    print("결과값은 %d 입니다."%s)

else:
    s=0
    for a in range(1,a+1,2):
        s +=a
    print("결과값은 %d 입니다." % s)