# 1. 导入模块
# import random
# 起别名
# import random as rd

# for i in range(100):
#   print(rd.randint(1, 100))

# 2. 导入模块中的功能
# from random import randint as rint
# 导入模块的所有功能
from random import *

for i in range(100):
  print(randint(1, 100))


if __name__ == '__main__':
  print("手写模块测试代码放在这个条件中")