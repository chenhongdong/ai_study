# __方法名__，用于定义类的特殊行为，这些就被称为是魔法方法，如：__init__
# 魔法方法是不需要我们手动调用，Python会在合适的时机自动调用。

# 常用魔法方法
# __init__  初始化方法
# __str__   字符串表示的方法
# __eq__    比较两个对象是否相等
# __lt__, __le__, __gt__, __ge__    支持两个对象的比较，分别为小于、小于等于、大于、大于等于


class Car:
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        self.price = price
    def runnning(self):
        print(f'{self.brand} {self.name} 正在告诉行驶中...')
    def __str__(self):
        return f'{self.brand} {self.name}，总价： {self.price}'
    def __eq__(self, other):
        return self.brand == other.brand and self.name == other.name and self.price == other.price
    def __lt__(self, other):
        return self.price < other.price


c1 = Car('问界', 'M7', 228000)
c2 = Car('问界', 'M8', 268000)

# c1.runnning()

print(c1)
print(c2)
print(c1 == c2)
print(c1 > c2)