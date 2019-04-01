class HomeWork:

    # 雷属性
    author = 'bh'

    def __init__(self, name):
        self.name = name
        self.date = '20190401'

    # 实例方法
    def get(self):
        print(self.name, self.date)

    # 类方法
    @classmethod
    def c_print(cls):
        print('在类方法里使用cls访问雷属性-------', cls.author)

    # 静态方法
    @staticmethod
    def s_print():
        print('没有cls无法访问雷属性')


# 类调用类属性
print(HomeWork.author)
# 穿件对象
h = HomeWork('second')
# 对象调用雷属性
print(h.author)
# 使用类修改雷属性
HomeWork.author = 'yiyi'
print(HomeWork.author, h.author)
# 对象无法修改类属性
h.author = 'bh'
print(h.author, HomeWork.author)

# del h.author
# print(h.author)
