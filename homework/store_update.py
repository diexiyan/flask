'''
正常学员：【零基础】
    电商项目，完整功能。
    用户相关：注册、登录、修改登录密码、完善个人资料【昵称】
    商品相关：购买[库存不足、金额不足...][扩展：积分]
    休闲小游戏：【石头、老虎、数字】【积分】

'''
import os,time,sys,random
users={'1':{'account':'1','pswd':'1','nickname':'1','jifen':100}}
user_index=0
while True:
    time.sleep(1)#
    os.system('cls')
    print("                欢迎来到电商首页，开始您的用户体验吧...     ")
    print("----------------------------------------------------------------------\n")
    print("                        1.登录                                        \n")
    print("                        2.新用户注册\n"                                   )
    print("                        3.退出系统\n"                                     )
    print("----------------------------------------------------------------------\n")
    
    print("若你已经注册过账号，可以登录，请输入1；\n\n若您还没有账号，请注册账号，输入2；\n\n若你想要退出系统，请输入3；\n")
    index_choice=input("请输入您的选择...")
    if index_choice=="1":
        while True:
            # os.system('cls')
            print(users)
            dl_account=input("请输入您的登录用户名...")
            dl_pswd=input("请输入您的登录密码!")
            # 判断是否登陆成功
            if (dl_account in users) and dl_pswd==users[dl_account]['pswd']:#成功
                    print(dl_account,"恭喜.........登陆成功...")
                    print("您的信息为：\n用户名： ",users[dl_account]['account'],"\t昵称：",users[dl_account]['nickname'],"\t积分：",users[dl_account]['jifen'])
                    # 修改密码
                    choice=input("您是否想要修改密码？输入Y,修改密码...")
                    if choice=="Y":
                        while True:
                            yl_pswd=input("请输入您原来的密码...(R,退出)")

                            # print(yl_pswd,xg_pswd,u[1])
                            if yl_pswd==users[dl_account]['pswd'] :
                                xg_pswd = input("请输入您的新密码...")
                                if xg_pswd==users[dl_account]['pswd']:
                                    print("您的新密码和原密码相同！不能修改密码")
                                else:
                                    users[dl_account]['pswd']=xg_pswd
                                    print("您的密码为： ",users[dl_account]['pswd'],"请重新登录!")
                                    break
                            elif yl_pswd=="R":
                                break
                            else:
                                print("您的密码不对，请重新输入！")
                            # break
                    else:
                        # 登陆后，选择购物或游戏
                        while True:
                            print("--------------------------------------------------------")
                            print("                  1.购物商场")
                            print("                  2.休闲小游戏")
                            print("--------------------------------------------------------")
                            choice=input("请输入您的选择...输入1，进入购物商场...输入2，进入休闲小游戏...(R键退出...)")
                            if choice=="1":
                                # 商场页面
                                product=[["苹果",4.3,50.0,"脆嫩多汁"],["香蕉",3.0,70.0,"又大又甜"]]
                                while True:
                                    print("--------------------------------------------------------")
                                    print(" \t商品名称\t商品单价\t库存\t介绍                 ")
                                    print(" \t",product[0][0],"\t",product[0][1],"\t",product[0][2],"\t",product[0][3]         )
                                    print(" \t",product[1][0],"\t",product[1][1],"\t",product[1][2],"\t",product[1][3])
                                    print("--------------------------------------------------------")
                                    # 购买物品
                                    gmw=input("请输入您要购买的物品：")
                                    gml=input("请输入您的购买量...")
                                    gml=float(gml)
                                    for i,pro in enumerate(product):
                                        if gmw==pro[0] and gml<=pro[2]:#可以购买
                                            money=pro[1]*gml
                                            while True:
                                                is_k=False
                                                print("您需要付:",money,"元")
                                                input_money=input("请输入您的钱...")
                                                input_money=float(input_money)
                                                # 判断金额足够
                                                if input_money>=money:
                                                    # 足够，小票
                                                    print("----------------------------")
                                                    print("您的购买信息如下：")
                                                    print("用户名：",users[dl_account]['account'])
                                                    print("购买物品：",pro[0])
                                                    print("单价：",pro[1])
                                                    print("应付：",money)
                                                    print("实付:",input_money)
                                                    print("找零：",input_money-money)
                                                    print("----------------------------")
                                                    # 减少库存
                                                    pro[2]-=gml
                                                    is_k=True
                                                    break
                                                else:
                                                    # 金额不足
                                                    print("您的金额不足，输入是，继续，否，退出")
                                                    jec=input("您的选择")
                                                    if jec=="是":
                                                        continue
                                                    else :
                                                        break

                                        elif gmw==pro[0] and gml>pro[2]:#库存不够
                                            print("库存不够...")
                                        # else:#
                                        #     print("没有这个选项哎，重新输入吧...")
                                        # if is_k:
                                        #     break#跳出for
                                    gwc=input("是否重新购物？输入是，重新购物;输入F，返回上级目录;输入R,退出系统;")
                                    if gwc=="是":
                                        # 重新购物
                                        continue
                                    elif gwc=="F":
                                        print("将要返回上级目录.........")
                                        break
                                    elif gwc=="R":
                                        print("系统将推出。。。")
                                        sys.exit(1)
                                    else:
                                        print("没有这个选项哎，重新输入吧...")   

                                choice=input("请输入您的选择...输入1，进入购物商场...输入2，进入休闲小游戏...(R键退出...)")
                                # if choice=="1":
                            # 游戏页面
                            elif choice=="2":
                                while True:
                                    print("--------------------------------------------------------")
                                    print("                  1.石头剪刀布")
                                    print("                  2.老虎棒子鸡")
                                    print("                  3.猜数字")
                                    print("--------------------------------------------------------")
                                    choice=input("每玩一局，减去5积分，赢得10积分，失败丢10积分！请输入您的选择...输入1/2/3...(R键退出...F返回上级目录)")
                                    # 石头剪刀布
                                    if choice=="1":
                                        print("电脑会自动生成一个值，与您输入的值作比较，判断您是否胜利...")
                                        # u[3]=100
                                        while True:
                                            users[dl_account]['jifen']-=5
                                            if users[dl_account]['jifen']>0:#判断生命值
                                                i=random.randint(1,3)
                                                # print(i)
                                                input_c=input("输入您的选择！")
                                                
                                                if (i==1 and input_c=="布") or (i==2 and input_c=="石头") or(i==3 and input_c=="剪刀") :
                                                    users[dl_account]['jifen']+=10
                                                    print("胜利！",users[dl_account]['jifen'])
                                                    
                                                elif (i==2 and input_c=="布") or (i==3 and input_c=="石头") or(i==1 and input_c=="剪刀"):
                                                    users[dl_account]['jifen']-=10
                                                    print("失败！",users[dl_account]['jifen'])
                                                    
                                                else:
                                                    print("平局！")
                                                # 判断是否继续
                                                i=input("是否继续，是，输入是，否则退出")
                                                if i=="是":
                                                    continue
                                                else:
                                                    break
                                            else:
                                                print("生命值不够！")
                                                break
                                        
                                    # 老虎帮子鸡
                                    elif choice=="2":
                                        print("电脑会自动生成一个值，与您输入的值作比较，判断您是否胜利...")
                                        # u[3]=100
                                        while True:
                                            users[dl_account]['jifen']-=5
                                            if users[dl_account]['jifen']>0:
                                                i=random.randint(1,4)
                                                # print(i)
                                                input_c=input("输入您的选择！")
                                                
                                                if (i==1 and input_c=="棒子") or (i==2 and input_c=="虫子") or(i==3 and input_c=="老虎")or(i==4 and input_c=="鸡") :
                                                    users[dl_account]['jifen']+=10
                                                    print("胜利！",users[dl_account]['jifen'])
                                                    
                                                elif (i==2 and input_c=="老虎") or (i==3 and input_c=="虫子") or(i==1 and input_c=="鸡")or(i==4 and input_c=="棒子"):
                                                    users[dl_account]['jifen']-=10
                                                    print("失败！",users[dl_account]['jifen'])
                                                    
                                                else:
                                                    print("平局！")
                                                # 判断是否继续
                                                i=input("是否继续，是，输入是，否则退出")
                                                if i=="是":
                                                    continue
                                                else:
                                                    break
                                            else:
                                                print("生命值不够！")
                                                break
                                    elif choice=="3":
                                        # u[3]-=15
                                        print("电脑自动生成一个值，您将进行猜，系统告诉您偏大偏小，直到猜中为止")
                                        num=random.randint(0,100)
                                        i=0
                                        while True:
                                            i+=1
                                            input_num=input("请输入您猜的值：")
                                            input_num=int(input_num)
                                            if num>input_num:#值偏小
                                                print("偏小了")
                                            elif num<input_num:
                                                print("偏大了")#偏小
                                            else:
                                                print("猜中了！")
                                                break
                                        # u[3]=u[3]+(i*)
                                    elif choice=="R":
                                        print("系统将退出...")
                                        time.sleep(3)
                                        sys.exit(1)
                                    elif choice=="F":
                                        break
                                    else:
                                        print("没有这个选项哎，重新输入吧...")
                            elif choice=="R":
                                print("系统将退出...")
                                time.sleep(3)
                                sys.exit(1)
                            else:
                                print("没有这个选项哎，重新输入吧...")
                    break#跳出for
            else :
                print("登录失败.........账号或密码错误，请重新输入...")
                # 是否退出
                choice=input("您是否想退出系统，输入R，退出")
                if choice=="R":
                    sys.exit(1)
    elif index_choice=="2":
        print("您来到了注册页面...")
        while True:
            time.sleep(1)
            os.system('cls')
            
            account=input("请输入您的用户名...")

            # 判断是否注册过用户名
            if account in users:
                print("该用户名已被注册，请重新输入...")
                continue
            pswd=input("请输入您的密码...")
            name=input("请输入您的昵称...")
            user={'account':account,'pswd':pswd,'nickname':name,'jifen':"daiding"}
            users[account]=user
            print("congrataltion,注册成功...")
            break
    elif index_choice=="3":
        print("您选择3，系统将退出...")
        sys.exit(1)
    else :
        print("没有这个选项，请重新操作...")
    