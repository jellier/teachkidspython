# 计算pizza包含税率的总价
num_pizza = eval(input("How many?"))

cost_pizza = eval(input("How much?"))

sub_total = num_pizza * cost_pizza

tax = sub_total * 0.08

total = sub_total + tax

# round( x [, n] )返回浮点数x的四舍五入值
print("Sub is " + str(sub_total) + " and total is " + str(round(total, 2)))
