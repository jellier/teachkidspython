# 第六课 和Python学数学 - 乘法口诀表

Hi,大家好，我是葫芦妈妈！又到了和葫芦妈妈一起学编程的时间了！

我们在二年级的时候就学过乘法了，你一定已经背得很熟了，今天我们要学习使用Python将乘法口诀打印出来


```Python
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
```


## 小结：
现在你应该：

* 学会了使用Python写一段打印九九乘法表的代码
* 学会使用了嵌套循环解决问题
* print