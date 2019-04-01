class HomeWork:
    pass


# 添加类属性
HomeWork.author = 'bh'
# 穿件对象测试
h1 = HomeWork()
print(h1.author)

# 添加示例属性
h1.name = 'third'
# 测试
# print(h1.name, HomeWork().name)#bh 'HomeWork' object has no attribute 'name'


# 添加方法

# 添加类方法
# 定义
@classmethod
def c_print(cls):
    print('这是一个类方法')


# 添加
HomeWork.c = c_print
# 调用
HomeWork.c()

# 添加静态方法
# 定义
@staticmethod
def s_print():
    print('这是一个静态方法')


# 添加
HomeWork.s = s_print
# 调用
HomeWork.s()


# 添加示例方法
# 定义
def o_print(self):
    print('this is a static method...')

# 添加
import types
h1.o = types.MethodType(o_print, h1)
# 调用
h1.o()

# 删除操作
# 删除方法
# del h1.o
# 删除属性
# del h1.name
# 测试
# h1.o()# 'HomeWork' object has no attribute 'o'
# print(h1.name)#'HomeWork' object has no attribute 'name'

# 第二种删除方法
delattr(h1, 'name')
# print(h1.name)#'HomeWork' object has no attribute 'name'
delattr(HomeWork, 'c')
# HomeWork.c()#AttributeError: type object 'HomeWork' has no attribute 'c'
