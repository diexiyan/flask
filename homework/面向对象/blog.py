'''
博客：
用户模块：
功能：登录、退出、注册、完善资料、修改密码
我注册了一个用户，登录后修改了密码，并完善了资料，最后退出了系统

'''
class User:
    '''定义了一个类'''

    def __init__(self,account, pswd, sex, age=14, phone=123, email=None):
        self.account = account
        self.pswd = pswd
        self.sex = sex
        self.email = email
        self.age = age
        self.phone = phone

    def input_login(self):
        '''输入登录密码'''
        acc=input("请输入您的账号!")
        pw=input("请输入您的密码!")
        return acc,pw

    def input_register(self):
        '''输入注册内容'''
        acc=input("请输入您的账号!")
        pw=input("请输入您的密码!")
        return acc,pw

    def input_pswd(self):
        '''输入修改的新密码'''
        # yuanlai_pswd=input("情书")
        xiugai_pswd=input("请输入您的新密码!")
        return xiugai_pswd

class Core:
    def __init__(self,state):
        '''

        :param state: 系统状态
        '''
        self.state=state

    def show_index(self):
        '''展示首页·'''
        print('-------------------------------------------------')
        print('            1.login')
        print('            2.quit')
        print('            3.regedit')
        print('-------------------------------------------------')
        self.show()

    def show_login(self):
        '''展示登录菜单'''
        print('-------------------------------------------------')
        print('            1.修改密码')
        print('            2.完善信息')
        print('            3.退出')
        print('-------------------------------------------------')
        # res=self.show_info()##self
        self.c_input_info()


    def show(self):
        '''跳转到夏季菜单'''
        res=u_choice()
        fun_dict[res]()if res !=None else self.show()

    def ziliao_input(self):
        '''跳转到夏季菜单'''
        res=u_choice()
        info_dict1[res]()if res !=None else self.show()

    def c_input_info(self):
        res = u_choice()
        fun_dict1[res]() if res != None else self.show()

    def show_info(self):
        '''
        系统显示信息
        :return: 用户选择
        '''
        choice = input("请输入您的选择....")
        return choice

    def c_login(self):
        '''系统登录'''
        user=online
        print("开始您的登录........")
        acc,pw=user.input_login()
        if acc==user.account and pw==user.pswd:##
            print("登陆成功!!!")
            self.show_login()##
        else:
            print(acc, user.account, acc==user.account, pw, user.pswd, pw==user.pswd)
            print("登录失败!您输入的账号或密码有误,请重新输入!")
            return self.c_login()##

    def c_register(self):
        '''系统注册'''
        print("开始注册啦!!!")
        u=User(None, None, None)
        u.account,u.pswd=u.input_register()#接受用户输入的内容
        global online
        online = u
        print("注册成功", u.account, u.pswd)
        self.show_index()

    def c_pswd(self):
        '''修改密码'''
        online.pswd=online.input_pswd()
        print("修改成功!")
        print(online.pswd, online.account)

    def c_update_info(self):
        print("-----------------------------")
        print("您的信息如下:")
        print("您的用户名：", online.account)
        print("您的性别：", online.sex)
        print("您的年龄：", online.age)
        print("您的手机号：", online.phone)
        print("您的邮箱：", online.email)
        print("-----------------------------")
        res=input("请输入要修改的内容...age")
        # self.fun(res)#
        if res=='性别':
            if  res=='男' or res == '女':
                online.sex=input("请输入您的新内容!")
            else:
                print("输入错误!")
            print(online.sex)
        elif res=='年龄':
            if 0 <= res < 150:
                online.age=input("请输入您的新内容!")
            else:
                print("输入错误!")
            print(online.age)
        elif res == '手机号':
            if  len(res)==11 and res.isdigit():
                online.phone=input("请输入您的新内容!")
            else:
                print("输入错误!")
            # online.phone = input("请输入您的新内容!")
            print(online.phone)
        elif res=='邮箱':
            if res.endswith('@qq.com'):
                online.email=input("请输入您的新内容!")
            else:
                print("输入错误!")
            # online.email=input("请输入您的新内容!")
            print(online.email)
        else:
            print("没有这个选项，请重新输入!")
            return self.c_update_info()
        self.show_login()

    # def fun(self,choice):
    #     online.chioce=input("请输入您的新内容!")
    #     print(online.age, online.chioce)



def u_choice():
    choice=input("请输入您的选择...")
    return choice
def e():
    exit(0)
sys_c = Core('开始')

fun_dict={'1':sys_c.c_login,
          '2':e,
          '3':sys_c.c_register
          }
fun_dict1={'1':sys_c.c_pswd,
          '2':sys_c.c_update_info,
          '3':e
          }
info_dict1={'性别':sys_c.c_pswd,
          '年龄':sys_c.c_update_info,
          '手机号':e,
          '邮箱':e
          }
sys_c.show_index()