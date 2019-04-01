'''
user={username:'a','pswd':1,nicheng:'q'}
users={'a':user}
'''
users=dict({'123':{'username':'123','password':'123','nickname':'123'}})

while True:
    print(".................................................")
    print("\t\t欢迎来到系统首页！")
    print("\t\t 1.登录...")
    print("\t\t 2.注册...")
    print("\t\t 3.退出...")
    print(".................................................\n")

    choice=input("请输入您的选项!")

    if choice=="1":
        print("欢迎来到登录界面，开始您的体验!")
        while True:
            dl_account=input("请输入您的账号!(R键退出!)")
            dl_pswd=input("请输入您的密码!")
            print("-----------登录存在时用户密码----------------",type(users[dl_account]['password']))
            # print("-----------登录存在时用户账户----------------",users[dl_account],type(users[dl_account]))
            if (dl_account in users) and (dl_pswd==users[dl_account]['password']):
                print("登路成功!")
                break
            # elif dl_account in users and dl_pswd!=users[dl_account]['password']:
            #     print("密码错误，重新输入!")
            # elif dl_account=="R":
            #     break
            else:
                print("账号错误！重新输入!")


    elif choice=="2":
        while True:
            print("欢迎注册，注册完成后您可以进行操作!")
            account=input("请输入您的账户!")
            if account in users:
                print("您的账号已存在，请重新输入!")
                # break
            else:
                pswd=input("请输入您的密码!")
                nickname=input("请输入您的昵称!")
                user={'username':account,'password':pswd,'nickname':nickname}
                # users={account:user}#每注册一个，声明一个users
                # users[account]=[user]#
                users[account]=user
                print("注册成功!",users)
                break
    elif choice=="3":
        pass
    else:
        print("没有这个选项，请重新输入")
    # break

