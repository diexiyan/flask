'''
围棋棋盘上的芝麻重量
每个格子中芝麻的数量，是前一个格子的两倍
第一个格子，放一粒芝麻[一粒芝麻的重量：0.006g]
'''
#print((2 ** 173)*0.006)

#如果上述问题中，第一个格子的芝麻是2粒？
#print((2 ** 174)*0.006)

#案例开发：指定商品的购买流程
	#展示所有商品
	##要求用户输入购买数量
	#要求用户付款
	#找零并打印小票
	#要求：开发正确流程
pro=[["苹果",4.0,100.0,"物美价廉"],["香蕉",4.0,100.0,"物美价廉"]]
#pro=((("苹果",4.0),[100],("物美价廉")),(("香蕉",4.0),[100],("助消化")))
#不能用，100无法转换为浮点型：if buy_name==p[0][0] and buy_num<=float(str(p[1])):
#pro=((("苹果",4.0),[100],("物美价廉")),(("香蕉",4.0),[100],("助消化")))
#print(pro[0][1])
#print((str(pro[0][1])))
#print("j")
#print(float((str(pro[0][1]))))

while True:
    print("........................................................")
    print("\t", "商品名称", "\t", "商品单价", "\t", "商品库存", "\t", "商品介绍")
    print("\t  ", pro[0][0], "\t      ", pro[0][1], "\t     ", pro[0][2], "\t", pro[0][3])
    print("\t  ", pro[1][0], "\t      ", pro[1][1], "\t     ", pro[1][2], "\t", pro[1][3])
    print("........................................................")
    buy_name=input("输入您要购买的物品！（如：苹果则输入苹果）")
    buy_num=input("输入您购买的数量！")
    buy_num=float(buy_num)
    for p in pro:
        #购买
        if buy_name==p[0] and buy_num<=p[1]:
            money=buy_num*p[1]
            #pay=input("您应付",money,"请输入您的金额！")input只能有一个值
            print("您应该付￥",money,"元")
            while True:
                pay=input("请输入您的金额！（1,退出）")
                pay=float(pay)
                #判断金额是否足够
                if pay>=money:
                    change=pay-money
                    p[1]=p[1]-buy_num
                #打印小票
                    print("商品名称：",p[0][0])
                    print("商品单价：",p[0][1])
                    print("您应付：",money)
                    print("实付：",pay)
                    print("找零：",change)
                    break
                elif pay==1:
                    break
                else:
                    print("您的金额不够！请重新输入！")

            #库存不足
        elif buy_name==p[0][0] and buy_num>p[1]:
            print(buy_num,buy_name)
            print("库存不足，请重新输入！")
            rebuy=input("是否重新购买？输入是，重新购买！")
            if rebuy=="是":
                print("goumai")
                pass
        else:
            print(buy_num, buy_name)
            print("输入错误！")
        break









