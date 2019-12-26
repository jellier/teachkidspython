# 使用turtle库画几何图形

# 导入turtle模块
import turtle
# 调用画笔
t= turtle.Turtle()

# 画正方形
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.reset()

# 画三角形
t.left(120)
t.fd(100)
t.left(120)
t.fd(100)
t.left(120)
t.fd(100)
t.reset()

# 画圆
t.circle(40)
t.circle(-40)
t.reset()
# 画正多边形
t.circle(40, steps=5)
t.reset()
t.circle(-40, steps=3)
t.reset()

# 画点
t.dot(20)

turtle.done()