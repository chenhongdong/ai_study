def reg_stu(name: str, age: int, gender: str = '男', city: str = '北京'):
  print(f"注册学生：{name}, 年龄: {age}， 性别： {gender}, 所在城市： {city}")
  return { name, age, gender, city }

# 位置参数（优点：简洁，缺点：可读性差、易出错、维护难）——一般少于3个参数直接用
stu1 = reg_stu('张三', 18)
print(stu1)

# 关键字参数（优点：可读性高、易维护和扩展，缺点：繁琐）
stu2 = reg_stu(age=29, name='宝宝', gender='女', city='上海')
print(stu2)

# 位置 + 关键字 混合参数 —— 位置参数必须写在关键字参数前面
stu3 = reg_stu('李刚', 22, city="广州")
print(stu3)



# 不定长参数
# 基于位置参数 *args 封装到一个元祖中
# 基于关键字参数 **kArgs 封装到一个字典中
def calc_data(*args, **kArgs):
  min_num = min(args)
  max_num = max(args)
  avg_num = sum(args) / len(args)
  # 设置保留的小数位
  if kArgs.get('round') is not None:
    avg_num = round(avg_num, kArgs.get('round'))

  if kArgs.get('print'):
    print(f'最小值、最大值、平均值分别为：{min_num}、{max_num}、{avg_num}')

  return min_num, max_num, avg_num

# data = calc_data(2, 7, 9, 10, 45, 73, 37, 93, 111, 92, 222, round=2)
# print(data)
min, max, avg = calc_data(10, 20, 30, 50, 40, 60, 70, 80, 100, 90, 23, round=2, print=True)
print(min, max, avg)