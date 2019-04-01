'''

'''
import os,sys,time
# user={'account':"123",'pswd':"123",'nickname':"待定"}
# users={"123":user}
# artical={'title':"123",'author':"123",'content':"today id thesday...",'read_count':'0'}

users={}
articals={}
# online=None
def show_login():
    print("\t\t博客用户登录")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    print("\t\t1. 用户登录")
    print("\t\t2. 用户注册")
    print("\t\t3. 退出系统")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    choice=input("请输入您的选项:")
    return login_choice.get(choice)() if choice else show_login()
def show_index():
    print("\t\t博客用户首页")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    print("\t\t1. 查看所有文章")
    print("\t\t2. 查看个人文章")
    print("\t\t3. 发表文章")
    print("\t\t4. 个人资料维护")
    print("\t\t5. 返回登录菜单")
    print("\t\t6. 退出系统")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    choice=input("请输入您的选项:")
    return index_choice.get(choice)() if choice else show_login()


def register():
    account = input("请输入您的账号，该账号将作为您的登录账号!")
    if account in users:
        print("您的账号已存在，请使用其他账号!")
        return register()
    else:
        pswd = input("请输入您的密码!")
        user = {'account': account, 'pswd': pswd, 'nickname': "待定"}
        users[account] = user
        print("注册成功!")
        show_login()


def show_register():
    print("\t\t博客用户注册")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    print("\t根据提示信息，完成用户资料的录入")
    print("\t创建自己的账号，享受系统带来的乐趣吧.....")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    register()
def exit():
    sys.exit(1)
def login():
    account = input("请输入您的账号!")
    pswd = input("请输入您的密码!")
    if (account in users)and pswd==users.get(account).get('pswd'):#
        global online
        online = users.get(account)
        print(users)
        print("登陆成功!")
        show_index()
        return True
    else:
        print("账号或密码错误，请重新输入!")
        return login()#
login_choice={
    "1":login,
    "2":show_register,
    "3":exit
}


def public_articals():
    global articals
    title = input("请输入您的标题!")
    if title in articals:
        print("您的标题已存在，请使用其他标题!")
        return public_articals()
    else:
        author = input("请输入您的名字!")
        content = input("请输入您的内容!")
        artical = {'title': title, 'author': author, 'content': content, 'read_count': 0}
        articals[title] = artical
        print(articals)
        print("发布成功!")
        show_index()


def look_all_articals():
    print("标题\t\t\t作者")
    for i in articals:
        print(i,str(articals.get(i).get('author')).ljust(18))#
    title=input("请输入您要看的题目:(R)键返回上级目录")
    if title in articals:
        articals[title]['read_count']+=1
        print("标题：",articals.get(title).get('title'))
        print("作者：",articals.get(title).get('author'))
        print("阅读次数：",articals.get(title).get('read_count'))
        print("内容：",articals.get(title).get('content'))
    elif title=="R":
        show_index()
    else:
        print("您要看的文章不存在，请重新输入!")
        return look_all_articals()


def look_my_articals():
    print("标题\t\t\t作者")

    for i in articals :
        print(articals.get(i).get('author'), online.get('account'))
        if articals.get(i).get('author')==online.get('account'):#
            print(i, str(articals.get(i).get('author')).ljust(18))  #
            title = input("请输入您要看的题目:")
            if title in articals:
                articals[title]['read_count'] += 1
                print("标题：", articals.get(title).get('title'))
                print("作者：", articals.get(title).get('author'))
                print("阅读次数：", articals.get(title).get('read_count'))
                print("内容：", articals.get(title).get('content'))
            elif title == "R":
                show_index()
            else:
                print("您要看的文章不存在，请重新输入!")
                return look_my_articals()


def info_update():
    print(online)
    choice=input("请输入您的选项，输入1，修改密码；输入2，完善资料")
    return info_choice.get(choice)() if choice else print("没有这个选项，请重新输入")


def update():
    prior_pswd=input("请输入您原来的密码!")
    global online
    if prior_pswd==online.get('pswd'):
        new_pswd=input("请输入您新的密码!")
        online['pswd']=new_pswd#
        print(users)
        print("修改成功")
    else:
        print("您的密码不成功，请重新输入!")
        return update()
        show_login()


def achiece():
    global online
    print(online)
    nickname=input("请输入您的昵称!")
    online['nickname']=nickname
    print(users)
    show_login()


info_choice={##
    "1":update,
    "2":achiece
}
index_choice={##
    "1":look_all_articals,
    "2":look_my_articals,
    "3":public_articals,
    "4":info_update,
    "5":show_login,
    "6":exit
}
def engin():
    show_login()
engin()