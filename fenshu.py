# 利用交叉相乘法比较两个分数的大小

# step1.输入分数
m = input('请按照"分子/分母"的格式，输入第一个分数：')
n = input('请按照"分子/分母"的格式，输入第二个分数：')
# step2.获得分子和分母，交叉相乘
mList = m.split('/')
nList = n.split('/')

ji1 = int(mList[0]) * int(nList[1])
ji2 = int(nList[0]) * int(mList[1])
# step3.判断大小
if ji1 > ji2:
    print(m + ' > ' + n)
elif ji1 < ji2:
    print(m + ' < ' + n)
else:
    print(m + ' = ' + n)



