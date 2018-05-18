
numbers =  input("숫자 5개를 ,로 구분하여 입력하세요: ")
list = list()

list = numbers.split(",")

print(list)
print(len(list))
sum=0
for i in range(0,5):
    sum += int(list[i])

avg = sum/len(list)

print("합: %d, 평: %d"%(sum,avg))