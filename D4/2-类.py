# 类是具备相同属性和方法的模板

# 定义类
# class 类名:
#     pass

# 创建类
class Car:
    # 类属性
    wheel = 4   # 轮胎数量
    tax_rate = 0.1  # 购置税

    # __init__是初始化方法，会在对象创建时自动调用，可以设置对应的属性
    # self: 是第一个参数，表示当前所创建出来的实例对象
    def __init__(self, brand, name, price, color):
        # 实例属性
        self.brand = brand
        self.name = name
        self.price = price
        self.color = color
    def total_cost(self, discount, rate=0.1):
        total_cost = self.price * discount + rate * self.price
        return total_cost

# 创建对象
c = Car('BYD', '海豹08', 228000, 'grey')
# c.brand = 'Benz'
# c.name = 'E300'
# c.price = 300000
# c.color = 'black'
print(c.brand)
print('税费', c.tax_rate)
print(Car.wheel)

print(c.__dict__)   # 将对象中的所有属性以字典的形式输出出来
# 字典 -> {'brand': 'Benz','name':'E300','price':30000,'color':'black'}


c2 = Car('Benz', 'E300', 300000, 'black')
print(c2.__dict__)


class StudentRecord:
    def __init__(self, name, age, className):
        self.name = name
        self.age = age
        self.className = className

# 创建学生对象
s1 = StudentRecord('小明', 9, '三年二班')
s2 = StudentRecord('小杰', 11, '五年一班')
s3 = StudentRecord('小红', 10, '四年五班')
print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)