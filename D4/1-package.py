# 模块较多时，对模块进行管理

# 1.导入模块
# import utils.my_fun
# utils.my_fun.log1()


# from utils import my_fun
# my_fun.log4()

# 注意：如果通过通配符导入，需要在__init__.py文件中添加__all__=['my_fun','my_var']
# from utils import *
# my_fun.log3()
# name = my_var.NAME
# print(name)


# 2.导入模块中的功能
from utils.my_fun import log1, log2
log1()
log2()