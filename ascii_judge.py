# 获取用户输入的ASCII编码值，以空格分隔
input_str = input("请输入一组以空格分隔的ASCII编码值: ")

# 将输入字符串分割成单独的ASCII编码值
ascii_values = input_str.split()

# 初始化一个空字符串，用于存储转换后的字符
result = ""

# 遍历每个ASCII编码值并将其转换为字符，然后拼接到结果字符串中
for ascii_value in ascii_values:
    try:
        # 将ASCII编码值转换为整数
        code = int(ascii_value)

        # 将整数转换为字符并拼接到结果字符串中
        result += chr(code)
    except ValueError:
        print(f"无效的输入: {ascii_value}")

# 输出拼接完整的ASCII字符
print(f"转换后的字符: {result}")
