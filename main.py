from flask import Flask, redirect, request, make_response

app = Flask(__name__)
app.debug = True

from flask import render_template


# 服务器/端口处理
@app.route('/')
def index():
    # 渲染html页面
    return render_template('/index.html')


import orm_class,datetime


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template('/login.html')
    else:
        # post请求下获得from表单；get请求：request.args.get(id)
        uid = request.form['u']
        pwd = request.form['p']
        res = orm_class.selectuser(uid, pwd)

        # 添加成功,使用响应创建cookie
        if res:
            res_c = make_response(redirect('/ulist'))
            # 使用时间设置cookie
            res_c.set_cookie('id', request.form['u'], expires=datetime.datetime.now()+datetime.timedelta(days=7))
            return res_c
        # 添加失败
        else:
            return render_template('/login.html')


# 服务器接收请求，post是从register.html的form表单请求，在函数内经判断处理请求，做出响应：渲染登录页面
# get是从超链接中来的请求。响应：渲染注册页面；
# 当有多种方法时一般get用来渲染页面，post用来实现功能；一种方法时不做处理，直接渲染页面
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "GET":
        return render_template('/register.html')
    else:
        userid = request.form['ur']
        username = request.form['uname']
        # 为字符串去掉空格
        username = username.replace(" ", '')
        print(username)
        pwd = request.form['pwd']
        res = orm_class.insertuesr(userid, username, pwd)
        if res == -1:
            # resp = make_response('<script language = javascirpt >alert("插入失败");</script>')
            # print(res)
            # return resp
            return '插入失败，请重新输入!'
        else:
            return render_template('/login.html')


@app.route('/ulist')
def ulist():
    res = orm_class.selectgoods()
    # 向html页面传参
    return render_template('/ulist.html', goodslist=res)


# 超链接向程序传参
@app.route('/goodsxq/<id>')
def goodsxq(id):
    res = orm_class.selectgoodsone(id)
    return render_template('/goodsxq.html', g=res)


@app.route('/addl', methods=['POST', 'GET'])
def addl():
    if request.method == 'GET':
        return render_template('/addl.html')
    else:
        try:
            sg = request.form['sg']
            num = request.form['num']
            # 判断是否为数字
            if num.isdigit():
                res = orm_class.addorder(request.cookies.get('id'), sg, num)
                # 判断是否插入成功，有异常出现
                if res == -1:
                    return "添加失败！"
                else:
                    # 使用request获得cookie 查询我的订单
                    uid = request.cookies.get('id')
                    res, goodsall = orm_class.selectOrder(uid)
                    return render_template('/dell.html', order=res, goodsall=goodsall)
            else:
                return '添加失败，数量应该用整数'
        except:
            return "内容不能为空!"


@app.route('/dell/<id>')
def dell(id):
    orm_class.deleteorder(id)
    uid = request.cookies.get('id')
    res, goodsall = orm_class.selectOrder(uid)
    return render_template('/dell.html', order=res, goodsall=goodsall)


@app.route('/upl/<id>', methods=['POST', 'GET'])
def upl(id):
    if request.method == 'GET':
        name, num = orm_class.selectnumname(id)
        return render_template('/upl.html', name=name, num=num, id=id)
    else:
        # try:
        num = request.form['num']
        # 判断数量是否为字符串 或者为 空字符串
        if num == "":
            return '数量不能为空'
        else:
            if num.isdigit:
                orm_class.upoder(id, num)
                uid = request.cookies.get('id')
                res, goodsall = orm_class.selectOrder(uid)
                print(num, type(num))
                return render_template('/dell.html', order=res, goodsall=goodsall)
            else:
                return '数量必须为数字!'


@app.route('/wd')
def wd():
    uid = request.cookies.get('id')
    res, goodsall = orm_class.selectOrder(uid)
    return render_template('/dell.html', order=res, goodsall=goodsall)


@app.route('/me')
def me():
    uid = request.cookies.get('id')
    user = orm_class.selectuserbyid(uid)
    return render_template('/me.html', user=user)


@app.route('/outme')
def outme():
    # 响应：1.必须返回response对象，作为响应来恢复请求
    # 2.make_response方法内必须使用重定向，再次请求，否则响应
    rep = make_response(redirect('/'))
    rep.delete_cookie('id')
    return rep


@app.route('/js/<oid>')
def js(oid):
    # 删除订单，减少产品数量
    res = orm_class.wjs(oid)
    if res == -1:
        return '库存不够，结算失败!'
    else:
        return redirect('/ulist')
# 慎重使用redirect:此方法向服务器发出请求会执行对应端口route('/,,,')下的方法即执行响应功能，不能接受参数；当在get中使用时会发生重定向次数多的错误
#                     与retem...的区别：前者发出请求，使用响应或需要使用响应中的功能时使用，且不能传参；后者只渲染页面


if __name__ == "__main__":
    # 添加一个端口号，防止多个程序同时运行时被占用端口号；若发生运行程序后不进行刷新
    app.run(port=8860)
