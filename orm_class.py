from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:123456@localhost/hbh",
                                    encoding='utf8',echo=False)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)

from sqlalchemy import Column, Integer, String, ForeignKey


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, nullable=False, primary_key=True)
    uname = Column(String(255))
    pwd = Column(String(255),nullable=False)


class Goods(Base):
    __tablename__ = 'goods'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    gname = Column(String(255), nullable=False)
    num = Column(Integer, nullable=False, server_default='100')
    price = Column(Integer, nullable=False, server_default='20')


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    gid = Column(Integer, ForeignKey('goods.id'), nullable=False)
    num = Column(Integer, nullable=False, server_default='1')

# Base.metadata.create_all(bind=engine)

from sqlalchemy.orm.session import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

goodslist = ["苹果", "梨", "香蕉"]
# for g in goodslist:
#     print(g)
    # session.add(Goods(id=0, gname=g))

session.commit()
from hashlib import sha1


def insertuesr(id=id, name=None, pwd='123456'):
    # 新建对象，否则会对加密后的密码进行拼接
    s = sha1()
    s.update(pwd.encode('utf8'))
    pwd = s.hexdigest()
    # 插入失败，处理异常如，id为空
    try:
        session.add(User(id=id, uname=name, pwd=pwd))
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        return -1
    finally:
        session.close()


def selectuser(id,pwd):
    # 新建对象，避免以前的密码被拼接
    s1 = sha1()
    s1.update(pwd.encode('utf8'))
    pwd = s1.hexdigest()
    row = session.query(User).filter(User.id == id, User.pwd == pwd).first()
    return row


def selectgoods():
    res = session.query(Goods).all()
    return res


def selectgoodsone(id):
    res = session.query(Goods).filter(Goods.id == id).first()
    return res


def addorder(uid, gid, num):
    # 处理异常
    try:
        session.add(Order(id=0, uid=uid, gid=gid, num=num))
        session.commit()
    except Exception as e:
        print(e)
        return -1
    finally:
        session.close()
    # return


def deleteorder(id):
    session.query(Order).filter(Order.id == id).delete()
    session.commit()


def selectOrder(id):
    res = session.query(Order).filter(Order.uid == id).all()
    goodsall = session.query(Goods).all()
    return res, goodsall


def selectnumname(id):
    obj = session.query(Order).filter(Order.id == id).first()
    num = obj.num
    gname = session.query(Goods).filter(Goods.id == obj.gid).first().gname
    return gname, num


def upoder(id,num):
    try:
        obj = session.query(Order).filter(Order.id == id).first()
        obj.num = num
        session.commit()
    except:
        session.rollback()
        return -1


def selectuserbyid(id):
    return session.query(User).filter(User.id == id).first()


def wjs(oid):
    obj = session.query(Order).filter(Order.id == oid).first()
    session.query(Order).filter(Order.id == oid).delete()
    goods = session.query(Goods).filter(Goods.id == obj.gid).first()
    # 判断库存
    if goods.num > obj.num:
        goods.num = goods.num - obj.num
        session.commit()
    else:
        # 回滚
        session.rollback()
        return -1
