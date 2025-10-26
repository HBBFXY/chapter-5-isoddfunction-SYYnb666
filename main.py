def isOdd(param):
    # 1. 先判断参数是否为整数类型；2. 再判断该整数是否为奇数
    return isinstance(param, int) and param % 2 != 0
param = input("请输入一个参数：")
if isOdd(param):
    print("Truse")
else:
    print("False")
