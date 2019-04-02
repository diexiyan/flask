"""

"""
def fun1(a):
    def fun2(b):
        nonlocal a# 添加关键字声明使用外部函数变量
        a += 1
        return a+b
    return fun2

f = fun1(10)
print(f(20)) #31
print(f(20)) #32
