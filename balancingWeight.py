# 砝码问题原理参考：https://www.xuebuyuan.com/1281379.html
# 乐乐课堂的讲解：https://wenku.baidu.com/video/course/v/V_47766bd97f1922791688e868
# 4个砝码，每个重量都是整数克，总重量为40克，放在天平上可以称出1～40克的物体。求这4个砝码各多少克。 1-3-9-27
# 3个砝码，每个重量都是整数克，总重量为13克，放在天平上可以称出1～13克的物体。求这3个砝码各多少克。 1-3-9

# 解题思路
# 首先要明确砝码可以放在天平的一侧，也可以放在两侧
# 如果砝码放在一侧 物体重量=砝码盘砝码重量相加
# 如果砝码放在两侧，物体重量=砝码盘砝码重量-物体盘砝码重量
# 所以放一边要算和，放两边要算差

# 设砝码的重量分别为w1,w2,w3
# w1+w2+w3= 13
# w1、 w2 、 w3均>0,且互不相等  ==> 不相等肯定有大有小，假设 0< w1<w2<w3<w4

# 从1～13，任意一个数，都应该能找到相应的砝码放置方法。
# 砝码只有3个，且每次称重时，这3个砝码只能出现0次或者1次，且砝码要么在物体盘，要么在砝码盘。
# 假设砝码在物体盘，认定其出现-1次
# 假设砝码在砝码盘，认定其出现1次
# 若该次称重，不需要该砝码，认定其出现0次

# ======================第一版===============================
# # 判断当前天平两侧是否相等
# def can_cal(w1, w2, w3, weight):
#     scope = [-1, 0, 1]  # -1代表放在物体盘，0代表不使用该砝码，1代表放在砝码盘
#     # num = 0
#     for x1 in scope:
#         # print('====')
#         for x2 in scope:
#             for x3 in scope:
#                 # num += 1
#                 # print('w1=', w1, ' w2=', w2, ' w3=', w3, ' x1=', x1, ' x2=', x2, ' x3=', x3, '  weight=', w1 * x1 + w2 * x2 + w3 * x3, '  num= ', num)
#                 if w1 * x1 + w2 * x2 + w3 * x3 == weight:
#                     # 跳出嵌套循环不能使用break，break只能跳出当前循环，所以此处要用return
#                     return True
#     return False
#
# # 判断当前组合是否能满足【1-13】种重量
# def has_thirteen(w1, w2, w3):
#     # 定义一个空列表来保存当前砝码组合下能得到哪些重量值
#     weight = []
#     # 遍历重量列表，如果当前砝码组合可以计算出当前的重量值，则把该重量值存储在weight列表中
#     for w in weight_list:
#         if can_cal(w1, w2, w3, w):
#             weight.append(w)
#     # 当weight列表中满足从1-13的所有情况，则返回True，否则返回False
#     if weight == weight_list:
#         return True
#     else:
#         return False
#
# # 主体逻辑
# weight_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# for w1 in weight_list:
#     for w2 in weight_list[w1:]:
#         for w3 in weight_list[w2:]:
#             # 判断当前组合是否可以得出【1-13】种重量，如果满足则打印出来，不满足继续循环
#             if has_thirteen(w1, w2, w3):
#                 print(w1, w2, w3)

# ===========================第一版 end==================
# ===========================第二版 start================

# 判断当前天平两侧是否相等
def can_cal(w1, w2, w3):
    side = [-1, 0, 1]  # -1代表放在物体盘，0代表不使用该砝码，1代表放在砝码盘
    temp = []
    cal_weight = []
    for x1 in side:
        for x2 in side:
            for x3 in side:
                temp.append(w1 * x1 + w2 * x2 + w3 * x3)

    temp = set(temp)
    for x in temp:
        if x>0:
            cal_weight.append(x)
    return cal_weight

# 主体逻辑
weight_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for w1 in weight_list:
    for w2 in weight_list[w1:]:
        for w3 in weight_list[w2:]:
            # 判断是否能表示1-13所有的情况
            if can_cal(w1, w2, w3) == weight_list:
                print(w1,w2,w3)
