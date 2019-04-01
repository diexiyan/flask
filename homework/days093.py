import os,sys,time
no=0
no_m=0
comments={}
mess={}
users={'1':{'account':'1','pswd':'1','email':'q.@qq.com'}}
# articals={}
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
    print("\t\t7. 修改个人文章")
    print("\t\t8. 删除个人文章")
    print("\t\t9. 回收站")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    choice=input("请输入您的选项:")
    return index_choice.get(choice)() if choice else show_login()


def register():
    account = input("请输入您的账号，该账号将作为您的登录账号!")
    # email=input("请输入您的邮箱，注册完成后，您也可以使用邮箱登录!")
    # if email.endswith('@qq.com'):
    #     if (account in users) or (email in users):
    if account in users:
        print("您的账号已存在，请使用其他账号!")
    # else:
    #     print("您的邮箱已存在，请使用其他邮箱!")
        return register()
    else:
        pswd = input("请输入您的密码!")
        nickname=input("请输入您的昵称!")
        user = {'account': account, 'pswd': pswd, 'nickname':nickname,'email':'待完善'}
        users[account] = user
        print("注册成功!")
        update_email(account)
        show_login()
def update_email(account):
    email=input("请输入您的邮箱，完成后您可以使用邮箱登录!")
    i=email.endswith('@qq.com')
    if i==False:
        print("您的邮箱不正确，请重新输入!")
        update_email(account)
    for i in users.values():
        print(i.get('email'))
        if email==i.get('email'):
            print("您的邮箱已存在，请使用其他邮箱!")
            update_email(account)
            break
    else:
        # users[account]['email']=email
        users.get(account)['email']=email
        print("邮箱注册成功!")
        print(users)

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
    account = input("请输入您的账号或密码!")
    pswd =input("请输入您的密码!")
    for v in users.values():
        if ((account in users) or (account==v.get('email'))) and pswd==v.get('pswd'):#
            global online
            online = users.get(account)
            print(users)
            print("登陆成功!")
            show_index()
            return True
    else:
        print(v,account == v.get('email'),pswd==v.get('pswd') )

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

def look_artical(u=None):
    print("标题\t\t\t作者")
    for i in articals :
        if u!=None and (articals.get(i).get('author')==u.get('account')):#
            print(articals.get(i).get('title'), str(articals.get(i).get('author')).rjust(18))
        elif u==None:
            print(articals.get(i).get('title'), str(articals.get(i).get('author')).rjust(18))
    title = input("请输入您要看的题目:")

    if title in articals:
        articals[title]['read_count'] += 1
        print("标题：", articals.get(title).get('title'))
        print("作者：",articals.get(i).get('author'))
        print("阅读次数：", articals.get(title).get('read_count'))
        print("内容：", articals.get(title).get('content'))
        for c in comments.values():
            if c.get('ari_title')==a.get('title'):
                print(online.get('account'),"对您发表了评论：",c.get('comment'))
        return articals[title]
        print(articals[title])
    elif title == "R":
        show_index()
    else:
        print("您要看的文章不存在，请重新输入!")
        return look_my_articals()



def look_all_articals():
    res =look_artical()
    global a
    a=res
    # print("标题\t\t\t作者")
    # for i in articals:
    #     print(i,str(articals.get(i).get('author')).ljust(18))#
    # title=input("请输入您要看的题目:(R)键返回上级目录")
    # if title in articals:
    #     articals[title]['read_count']+=1
    #     print("标题：",articals.get(title).get('title'))
    #     print("作者：",articals.get(title).get('author'))
    #     print("阅读次数：",articals.get(title).get('read_count'))
    #     print("内容：",articals.get(title).get('content'))
    # elif title=="R":
    #     show_index()
    # else:
    #     print("您要看的文章不存在，请重新输入!")
    #     return look_all_articals()
    # if res.get('author')==online.get('account'):
    #     print("您无法评论或私信!")
    # else:
    choice=input("您是否想要私信，1，或者，评论，2,")
    return articals_choice.get(choice)() if choice else show_login()

def look_my_articals():
    res=look_artical(online)
    print(look_my_articals)
    return res

    # print("标题\t\t\t作者")
    #
    # for i in articals :
    #     print(articals.get(i).get('author'), online.get('account'))
    #     if articals.get(i).get('author')==online.get('account'):#
    #         print(i, str(articals.get(i).get('author')).ljust(18))  #
    #         title = input("请输入您要看的题目:")
    #         if title in articals:
    #             articals[title]['read_count'] += 1
    #             print("标题：", articals.get(title).get('title'))
    #             print("作者：", articals.get(title).get('author'))
    #             print("阅读次数：", articals.get(title).get('read_count'))
    #             print("内容：", articals.get(title).get('content'))
    #         elif title == "R":
    #             show_index()
    #         else:
    #             print("您要看的文章不存在，请重新输入!")
    #             return look_my_articals()


def info_update():
    print(online)
    choice=input("请输入您的选项，输入1，修改密码；输入2，完善资料")
    return info_choice.get(choice)() if choice else print("没有这个选项，请重新输入")


def update():
    prior_pswd=input("请输入您原来的密码!")
    global online
    if prior_pswd==online.get('pswd'):
        new_pswd=input("请输入您新的密码!")
        if prior_pswd==new_pswd:
            print("您的新密码与老密码相同，请重新输入!")
            return update()
        else:
            online['pswd']=new_pswd#
            print(users)
            print("修改成功")
            login()
    else:
        print("您的密码不成功，请重新输入!")
        return update()
        show_login()


def achiece():
    global online
    print(online)
    photo=input("请输入您的手机号!")
    if photo.isdigit()==False or len(photo)!=11:
        print("您的手机号输入错误!")
        return achiece()
    print(photo.isdigit()==False,len(photo)!=11,photo.isdigit()==False or len(photo)!=11)
    sex=input("请输入您的性别!输入1，为女其它选项为男")
    if sex=='1':
        sex='女'
    else:
        sex="男"
    age=input("请输入您的年龄!")
    if age.isdigit()==False:
        print("输入错误，请重新输入")
        return achiece()
    online['photo']=photo
    online['sex']=sex
    online['age']=age
    print(users)
    show_login()


info_choice={##
    "1":update,
    "2":achiece
}


def comment():
    global no
    no+=1
    str_comment=input("请输入您的评论!")
    comment={'no':no,'comment':str_comment,'ari_title':a.get('title'),'account':online.get('account')}
    comments[no]=comment
    print()
    show_index()#


def message():
    choice=input("请输入您的选择，查看私信，11,查看已读，12，查看未读，发送私信，2，其他键返回上级目录")
    if choice=='11':
        for v in mess:
            if mess.get(v).get('rec_account')==online.get('account'):#该用户信息
                if mess.get(v).get('state'):#yidu
                    print(mess.get(v))
    elif choice=='12':
        for v in mess:
            if mess.get(v).get('rec_account')==online.get('account'):#该用户信息
                if mess.get(v).get('state')==0:#yidu
                    print(mess.get(v))
    elif choice=='1':
        if a.get('author') == online.get('account'):
            print("您无法为自己添加私信!")
        else:
            global no_m
            no_m += 1
            str_mes = input("请输入您的私信!")
            mes = {'no_m':no_m,'state': 0, 'mes': str_mes, 'rec_account': a.get('author'), 'send_account': online.get('account')}
            mess[no_m] = mes
            print(a.get('account'),a)
            print(mess)
        show_index()

    elif choice=='2':
        str_mes = input("请输入您的消息!")
        mes = {'state': 0, 'mes': str_mes, 'rec_account': a.get('author'), 'send_account': online.get('account')}
        mess[no] = mes
        print(mess)
        show_index()



articals_choice={
    '1':message,
    '2':comment
}


def update_artical():
    print(articals)
    res=look_my_articals()
    choice=input("是否需要修改该文章?输入是，则会修改该文章!")
    if choice=='是':
        c=input("请输入您要修改的地方，选择1，修改名字!")
        if  c=="1":
            title = input("请输入您的标题!")
            if title in articals:
                print("您的标题已存在，请使用其他标题!")
                return update_artical()
            else:
                res['title']=title

        else:
            content=input("请输入您的内容!")
            res['content']=content
        print(articals, "修改成功")
        return update_artical()
    else:
        show_index()


def del_artical():
    print(del_artical)
    res=look_my_articals()
    recyle_bin[res.get('title')]=res
    print(articals,recyle_bin)
    articals.pop(res.get('title'))
    print(articals, recyle_bin)
    show_index()


def en2():
    print(recyle_bin)
    choice = input("请输入文章名字:")
    choice_c=input("请选择恢复文章，1或永久删除文章删除")
    if choice_c=="1":
        articals['title'] = recyle_bin[choice]
        print(articals)
        print("恢复成功")
    else:
        print("删除成功")
    recyle_bin.pop(choice)
    print(recyle_bin)
    show_index()

index_choice={##
    "1":look_all_articals,
    "2":look_my_articals,
    "3":public_articals,
    "4":info_update,
    "5":show_login,
    "6":exit,
     '7':update_artical,
     '8':del_artical,
     '9':en2
}
articals={'jijij':{'title':'jijij','author':'1','content':'hduhscusuysid','read_count':0},'正在调试':{'title':'正在调试','author':'1','content':'hduhscusuysid','read_count':0},'jhdjks':{'title':'jhdjks','author':'jkk','content':'hduhscusuysid','read_count':0}}
recyle_bin={}
def engin():
    show_login()
engin()

