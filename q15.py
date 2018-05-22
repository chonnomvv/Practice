#
# list = list(range(1,100))
#
#
# string = ""
# for i in list:
#     listt = str(i)
#     if listt.startswith("3")== 1 or listt.startswith("6") ==1 or listt.startswith("9") ==1:
#         if listt.find("3")==1 or listt.find("6")==1 or listt.find("9")==1:
#             string = "짝"*2
#         else:
#             string = "짝"
#     elif listt.find("3") == 1 or listt.find("6") == 1 or listt.find("9") == 1:
#         if listt.startswith("3")==1 or listt.startswith("6")==1 or listt.startswith("9")==1:
#             string = "짝"*2
#         else:
#             string = "짝"
#     elif ("33" in listt) == True  or ("66" in listt)==True or ("99" in listt) == True:
#         string = "짝"*2
#     else:
#         string = ""
#
#     print(listt + string)


check = [3, 6, 9]

for i in range(1, 100):
    count = 0
    first = i // 10 #10 자리
    second = i % 10 #1 의자리
    # print(first, second)
    if second in check:
        count = 1
        
    elif first in check:
        count = 1

    if second in check and first in check:
        count = 2

    if count == 1:
        print(i, "짝")
    elif count ==2:
        print(i,"짝짝")