# 打印乘法口诀表，讲嵌套循环

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (j, i, j * i), end="  ")
    print('\n')


i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d*%d=%d' % (j, i, j * i), end="  ")
        j += 1
    print()
    i += 1
