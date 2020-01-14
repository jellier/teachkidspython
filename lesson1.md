# 第1课：从Hello World开始

Hi,大家好，我是葫芦妈妈。今天我们就要正式开始学习Python编程了   

课前你应该都已经安装好了Python的开发环境，那现在请按照课前提示点击IDLE进入到Python Shell吧。  
然后选择File->New File命令，就会打开一个Python编辑器窗口，其顶部带有一个Untitled标题。

## 从 hello,world开始
按照惯例，程序员在学习一门语言时，写的第一行代码通常是 “hello , wold” 。这行代码非常简单，它只是向计算机屏幕输出了 “hello , wold”这样一句字符串。  

在Python的中向屏幕输出这句话要用print(‘hello,world')，print在英文中是打印的意思，也就是告诉计算机请打印出hello,world这几个字。我们一起来试一下，注意这里输入的时候一定要将输入法切换到英文输入状态哦   

![print('hello world')](pic/p-1-1.png)

print是Python语言的输出函数，在编辑器里函数用紫色显示，hello world是一串字符串，在编辑器里字符串默认用绿色显示。

接着，点击编辑器窗口上方的菜单Run—>Run Module   
![Run Module](pic/p-1-2.png)

这时会弹出一个对话框，提示你要先保存程序代码   
![save your code 1](pic/p-1-3.png)
  
![save your code 2](pic/p-1-4.png)
点击“确定”或者“OK”按钮，在弹出的对话框中输入文件名hello.py，选个保存的目录（这里我选的是桌面，你可以请爸爸妈妈帮忙建个你专属的文件夹）。保存后Python Shell窗口就会被激活，你的第一行代码将被执行，执行结果显示在<<< 提示符后面   
![show your code](pic/p-1-5.png)    

好了，你已经编写完第一个Python程序了。

当程序可以正常运行后，试着修改代码中的一些值，观察代码的变化，可以直观的了解代码的作用，    
比如我把 hello, wold改成 hello, 葫芦，print(“hello,葫芦”)    
这里“葫芦”是中文，输入的时候要注意中英文切换，在Python中只有***引号里面的字符串和注释中可以有中文字符***，其他不管是关键字还是字符（比如括号，引号）都必须是***英文***哦    
![show your code](pic/p-1-6.png) 

## 更进一步
我们再来给代码加点好玩的，让程序代码询问电脑前的用户姓名，然后把名字打印出来    
回到编辑窗口，输入下面几行代码，注意中英文切换    
```Python
# 输入你的姓名
name = input("请问你叫什么名字？")
print('hello,',name)
```
![input name](pic/p-1-10.png) 