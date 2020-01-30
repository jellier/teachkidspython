'''
三对情侣参加婚礼，三个新郞为 A、 B、 C，三个新娘为 X 、 Y 、 Z。有人不知道谁和谁结婚，于是询问了六位新人中的三位，但听到的回答是这样的：
A 说他将和 X 结婚； X 说她的未婚夫是 C； C 说他将和 Z 结婚。这人听后知道他们在开玩笑，全是假话。请编程找出谁将和谁结婚。
'''

bride = ['X', 'Y', 'Z']
for A_bride in bride:
    for B_bride in bride:
        for C_bride in bride:
            if A_bride != B_bride and B_bride != C_bride and C_bride != A_bride and A_bride != 'X' and C_bride != 'X' and C_bride != 'Z':
                print('A与' + A_bride + '结婚')
                print('B与' + B_bride + '结婚')
                print('C与' + C_bride + '结婚')




# 原代码
# bride = ['X','Y','Z']
# for A in bride:
#   for B in bride:
#     for C in bride:
#       if A != B and B != C and C != A:
#         if A != 'X' and C != 'X' and C != 'Z':
#           print('A与' + A + '结婚')
#           print('B与' + B + '结婚')
#           print('C与' + C + '结婚')

# 这里的第二个if条件判断是个难点，有点tricky