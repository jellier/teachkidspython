# 二进制转换为十进制
# pow(x, y[, z]),函数是计算x的y次方，
# 如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z
# 也可以用 math模块的pow方法：
# import math
# math.pow( x, y )
# 注意：pow() 通过内置的方法直接调用，内置方法会把参数作为整型, 而math 模块则会把参数转换为 float

# userInput = input("请输入一个二进制数：\n")
#
# def binary2decimal():
#     sum = 0
#     s = list(userInput)
#     s.reverse()
#     for i in range(len(s)):
#         sum += int(s[i]) * pow(2, i)
#     print("此数对应的十进制数是：", sum)
#
#
# def binary2decimal2():
#     sum = 0
#     binaryLen = len(userInput)
#     for i in range(binaryLen):
#         # sum += int(userInput[binaryLen - 1 - i]) * pow(2, i)
#         sum += int(userInput[i]) * pow(2, binaryLen - 1 - i)
#     print("此数对应的十进制数是：", sum)
#
# print('==========')
# binary2decimal()
# print('==========')
# binary2decimal2()
# print('=====验证：=====')
# print(int(userInput, 2))
#

# 第一步：输入(input)--告诉程序你的二进制数
binary = input("请输入一个二进制数：")

# 第二步：处理(process) --将二进制数转化为十进制数
decimal = 0
power = 0
binaryLen = len(binary)

for i in range(0, binaryLen):
    power = binaryLen - 1 - i
    decimal += int(binary[i]) * pow(2, power)

# 第三步：输出(output) –将十进制数的结果打印到屏幕上
print("对应的十进制数是：", decimal)

