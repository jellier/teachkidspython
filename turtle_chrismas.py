# 使用turtle库画一棵圣诞树

# 导入turtle模块
import turtle

# 询问用户圣诞节到了吗？
isChris =input('圣诞节到了吗？')
# 根据输入结果判断是否显示圣诞背景图
if isChris == 'yes':
    # 设置屏幕背景
    screen = turtle.Screen()
    screen.setup(600, 400)
    screen.bgpic('pic/chrismasbg.gif')

# 调用画笔
t= turtle.Turtle()
# 画树冠
t.penup()
t.goto(0,120)
t.pendown()
t.fillcolor("DarkGreen")
t.begin_fill()
t.goto(-60,-100)
t.goto(60,-100)
t.goto(0,120)
t.end_fill()

# 画树干
t.penup()
t.goto(0,-100)
t.pendown()
t.pensize(30)
t.color('Brown')
t.goto(0,-170)

# 画五角星
t.penup()
t.goto(5,120)
t.pendown()

t.pensize(3)
t.color('Yellow', 'Gold')
t.begin_fill()
for i in range(5):
    t.fd(20)
    t.right(144)
    t.fd(20)
    t.left(72)
t.end_fill()
t.hideturtle()


turtle.done()