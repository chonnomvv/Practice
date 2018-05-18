
list = list(range(1,100))


string = ""
for i in list:
    listt = str(i)
    if listt.startswith("3")== 1 or listt.startswith("6") ==1 or listt.startswith("9") ==1:
        if listt.find("3")==1 or listt.find("6")==1 or listt.find("9")==1:
            string = "짝"*2
        else:
            string = "짝"
    elif listt.find("3") == 1 or listt.find("6") == 1 or listt.find("9") == 1:
        if listt.startswith("3")==1 or listt.startswith("6")==1 or listt.startswith("9")==1:
            string = "짝"*2
        else:
            string = "짝"
    elif listt.find("33")==1 or listt.find("66")==1 or listt.find("99")==1:
        string = "짝"*2
    else:
        string = ""
    print(listt + string)
