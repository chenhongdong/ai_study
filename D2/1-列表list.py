# 列表的特点是？
  # 元素可重复、有序、可以修改的

s = ["A", "C", "H", "K", "L", "B", "D", "X", "C", "U"]

# 切片操作 s[开始索引:结束索引:步长间隔]
#           默认0           默认1
c = s[0:5:1]
# c = s[:5:]  # 简写
print(c)  # ACHKL

c = s[0:5:2]
print(c)  # AHL

d = s[0:-2:1]
print(d)  # A-X



# 案例：合并两个列表并去重
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
# 1. 合并列表
# for n in num_list2:
#   num_list1.append(n)

# 解包：将列表容器的元素一个一个解开成独立元素
new_list = [*num_list1, *num_list2]
# 组包：将多个值合并到一个容器

# 更简单的合并列表
new_list2 = num_list1 + num_list2


# print(num_list1)
# 2. 去重
num_list = []

for n in new_list2:
  # 判断num_list中是否存在n元素，如果不存在就添加进去
  if n not in num_list: # in运算符 用来判断元素是否存在于列表中，如果存在则为True，不存在则为False
    num_list.append(n)

print("去重后的列表：", num_list)




# 例：生成1-20的平方列表
# 传统方式
nums = []
for i in range(1, 21):
  nums.append(i**2)

print(nums)

# 简化方式：列表推导式 --> 按照一定的规则快速生成一个列表的方法 --> 语法格式1：[要插入的值 for i in 序列/列表]
nums2 = [i**2 for i in range(1, 21)]

print(nums2)


# 例：从一个数字列表中提取所有的偶数，并计算平方，组成一个新的列表。
# 列表推导式 --> 按照一定的规则快速生成一个列表的方法 --> 语法格式2：[要插入的值 for i in 列表 if 条件]，if可选
nums3 = [12, 32, 45, 77, 80, 92, 33, 57, 97, 98, 110, 111, 122]
new_list = [i**2 for i in nums3 if i % 2 == 0]

print(new_list)


# 作业1：将如下多个列表合并为一个列表，并去重，排好序后输出到控制台
list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
list3 = ['W', 'A', 'S', 'D']

list = list1 + list2 + list3

new_list = []
for s in list:
  if s not in new_list:
    new_list.append(s)
new_list.sort()
print(new_list)


# 作业2：将如下列表中能被3 或 5整除的元素提出来，并获取这些数字对应的平方，组成新列表
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
new_list = [i**2 for i in list if i % 3 == 0 or i % 5 == 0]
print(new_list)


# 作业3：将如下列表中的正数提取出来，封装为一个新列表
list = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 35, -16, 87, -39]
list2 = [i for i in list if i > 0]
print(list2)