# 导入turtle模块，创建小画家Bob
import turtle
Bob = turtle.Turtle()
# “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”.
Bob.shape('turtle')

# 召唤魔法画布，让Bob变身
screen = turtle.Screen()
screen.register_shape('house30.gif')
Bob.shape('house30.gif')

# 开始画图
Bob.forward(100)

Bob.stamp()
Bob.left(90)
Bob.forward(100)
Bob.left(90)
Bob.stamp()

Bob.forward(100)
Bob.left(90)
Bob.stamp()

Bob.forward(100)
Bob.left(90)
Bob.stamp()







turtle.done()

