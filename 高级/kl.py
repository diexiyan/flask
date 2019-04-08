import requests
rep = requests.get('http://quote.stockstar.com/stock/ranklist_a_3_1_1.html')
# print(rep.text)
stra = rep.text
# 获取内容字符串
#

import re
ma1 = re.findall('tbody(.*?)</tbody>', stra, re.S) #?
# print(ma1)
# tr
trlist = re.findall('tr>(.*?)</tr>', ma1[0])
# print(trlist)
for t in trlist:
    # print(t)
    # alist = re.findall(r'<a href="//stock.quote.stockstar.com/(.*?).shtml">\1</a>', t)
    print(alist)
    namelist = re.findall(r'<a href="//stock.quote.stockstar.com/(.*?).shtml">(.*?)</a>', t)
    print(namelist[1][1])
    alist = re.findall(r'<span class="red">(.*?)</span>', t)
    print(alist[0])
