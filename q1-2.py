# print("Q1","="*200)
# number = 1
# for number in range(1,71):
#     if(number%5 ==0 and number%7==0):
#         print(number)
#
# print("Q2","="*200)


num = int(input("숫자를 입력하세요: "))
for i in range(1,num+1,1):
    for j in range(i,i+1):

      print(str(j)*i)
