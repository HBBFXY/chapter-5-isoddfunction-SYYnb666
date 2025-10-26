def isOdd(num):
    return isinstance(num, int) and num % 2 == 1

# 获取用户输入并处理
user_input = input("请输入一个值：")

try:
    # 尝试将输入转换为整数
    num = int(user_input)
    # 调用函数并输出结果
    print(isOdd(num))
except ValueError:
    # 如果无法转换为整数，直接返回False（符合函数"其他情况"的定义）
    print(isOdd(user_input))
