
menu = input("메뉴: ")

menu_list = {"오뎅":300,"순대":400,"만두":500}

if menu in menu_list.keys():
    print(menu,':',menu_list[menu])
else:
    print("없는 메뉴입니다.")