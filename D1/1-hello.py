print("######################")
print("###### Hello Python #####")
print("######################")
print("Hello")
print(type("Hello")) # str
print(type(1))
print(type(3.14))
print(type(True))
print(type(False))
print(type(None))

# 判断数据类型
num = 5.0
print(isinstance(num, int))
print(isinstance(num, float))
print(isinstance(num, bool))   

# 字符串格式化  %s 占位符
s1 = "人生苦短"
s2 = "我用AI"
print("再学习再就业 %s %s" % (s1, s2))

name = "小白"
age = 11
pro = "软件工程"
hobby = "Python，Java"
# print("大家好 我是 %s，今年 %s 岁，专业为 %s ，爱好是 %s" % (name, age, pro, hobby))


# 字符串格式化 f"内容{变量/表达式}"  推荐
print(f"大家好，我是 {name}，今年{age}")

print(10/4)
print(10//3)
print(10 ** 2)


x = int(input("请输入x的值："))
y = int(input("请输入y的值："))

print("x+y= ", x + y)

x = int(input("请输入x的值:"))
y = int(input("请输入y的值:"))
print("x+y= ", x + y)
