
print("숫자를 입력하세요")
Bnumber = -111111
print(type(Bnumber))
for i in range(1,6):

    number=int(input("숫자:"))

    print(type(number))
    if number>Bnumber:
        Bnumber = int(number)
    i += 1

print("최대값은" + str(Bnumber))

