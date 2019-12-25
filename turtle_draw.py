# 使用turtle库画一个小房子

# 导入turtle模块
import turtle
# 调用画笔
t= turtle.Turtle('turtle')

# 画正方形
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)

turtle.resetscreen()


# 画三角形
# 相对方式
t.left(120)
t.fd(100)
t.left(120)
t.fd(100)
t.left(120)
t.fd(100)
# 绝对方式
t.goto(100,100)
t.goto(150,0)
t.goto(0,0)
turtle.resetscreen()

# 画圆

t.circle(40)
t.circle(-40)

# 画正多边形
t.circle(40,steps=5)
t.circle(-40,steps=3)


turtle.done()