import random

a=1
while a==1:
    ran = random.randrange(1,100)
    print(ran)


    print("="*40)
    print(" [숫자 맞추기 게임] ")
    print("="*40)
    while 1:
     answer = int(input("숫자:"))
     if answer>ran:
         print("더 낮게")
     elif answer < ran:
         print("더 높게")
     elif answer==ran:
         print("정답!")
         if input("게임을 종료 하시겠습니까?(y/n)") == 'y':
             a=2
             break
         else:
             print("keep going")
             break