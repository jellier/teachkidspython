# 使用turtle库画一棵圣诞树
# 导入turtle模块
import turtle

isChris =input('圣诞节到了吗？')
if isChris == 'y':
    # 调用屏幕
    screen = turtle.Screen()
    screen.setup(600, 400)
    screen.bgpic('pic/chrismasbg.gif')

# 调用画笔
t= turtle.Turtle()
t.left(90)
t.color("DarkGreen")
# 画第一个三角形
t.penup()
t.goto(0,100)
t.pendown()
t.begin_fill()
t.goto(-60,-100)
t.goto(60,-100)
t.goto(0,100)
t.end_fill()

# 画树干
t.penup()
t.goto(0,-100)
t.pendown()
t.pensize(30)
t.color('SaddleBrown')
t.goto(0,-170)

# 画五角星
t.penup()
t.goto(0,100)
t.left(126)
t.pendown()

t.pensize(3)
t.color('Gold')
t.begin_fill()
for i in range(5):
    t.fd(20)
    t.right(144)
    t.fd(20)
    t.left(72)

t.end_fill()
t.hideturtle()


turtle.done()