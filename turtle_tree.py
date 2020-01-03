# 使用turtle库画一个金灿灿的五角星

# 导入turtle模块
import turtle
# 调用画笔
t= turtle.Turtle()
# 设置画笔粗细
t.pensize(3)
# 设置画笔颜色
t.color('Yellow', 'Gold')
# 填充五角星开始
t.begin_fill()
# 循环
for i in range(5):
    t.fd(20)
    t.right(144)
    t.fd(20)
    t.left(72)
# 填充五角星结束
t.end_fill()
# 画笔隐藏
t.hideturtle()

turtle.done()