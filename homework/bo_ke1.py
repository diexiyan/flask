'''
【个人资料维护】修改登录密码完善个人资料返回上一级【文章数据维护】
'''

import sys,time
def show_login():
    print("欢迎!!!")
    print(".........................................")
    print("            1 .用户登录")
    print("            2 .用户注册")
    print("            3 .退出系统")
    print(".........................................")

    choice=input("请输入您的选项:")
    if choice=="1":
        show_index()

    elif choice=="2":
        # 注册
        print("register")
    elif choice=="3":
        print("系统即将退出.......")
        time.sleep(2)
        sys.exit(1)
    else:
        print("没有这个选项，请重新输入!!!")
        show_login()

def show_index():
    print("欢迎!!!")
    print(".........................................")
    print("            1 .个人资料维护")
    print("            2 .文章数据维护")
    print("            3 .返回上一级")
    print("            4 .退出系统")
    print(".........................................")

    index_choice = input("请输入您的选项:")

    if index_choice == "1":
        print("index_choice", index_choice)
        update_myinfo()

    elif index_choice == "2":
        print("index_choice", index_choice)
        update_myartical()

    elif index_choice == "3":
        print("index_choice", index_choice)
        show_login()
    elif index_choice == "3":
        print("index_choice", index_choice)
        print("系统即将退出.......")
        time.sleep(2)
        sys.exit(1)
    else:
        print("index_choice", index_choice)
        print("没有这个选项，请重新输入!!!")
        show_index()

def update_myinfo():
    print(".........................................")
    print("            1 .修改登录密码")
    print("            2 .完善个人资料")
    print("            3 .返回上一级")
    print(".........................................")

    info_choice = input("请输入您的选项:")
    if info_choice == "1":
        print("info_choice", info_choice)
        print("修改登录密码")
        sys.exit(1)
    elif info_choice == "2":
        print("info_choice", info_choice)
        print("完善个人资料")
        sys.exit(1)
    elif info_choice == "3":
        print("info_choice", info_choice)
        show_index()
    else:
        print("info_choice", info_choice)
        print("没有这个选项，请重新输入!!!")
        show_index()

def update_myartical():
    print(".........................................")
    print("            1 .发表文章")
    print("            2 .查看所有文章")
    print("            3.查看个人文章")
    print(".........................................")

    artical_choice = input("请输入您的选项:")
    if artical_choice == "1":
        print("artical_choice", artical_choice)
        print("发表文章")
        sys.exit(1)
    elif artical_choice == "2":
        print("artical_choice", artical_choice)
        print("查看所有文章")
        sys.exit(1)
    elif artical_choice == "3":
        print("artical_choice", artical_choice)
        print("查看个人文章")
        sys.exit(1)
    else:
        print("artical_choice", artical_choice)
        print("没有这个选项，请重新输入!!!")
        show_index()

show_login()

































