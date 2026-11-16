
# 计算圆的面积
def circle_area(r):
  area = 3.14 * r * r
  return area

c_area = circle_area(10)
print(c_area)

# 计算长方形的面积
def rectangle_area(l, w):
  area = l * w
  return area

r_area = rectangle_area(10, 6)
print(r_area)

# 函数可以返回多个值,如果返回多个值,则返回的是一个元组
# 计算圆的面积和周长
def circle_area_len(r):
  area = 3.14 * r ** 2
  len = round(2 * 3.14 * r, 1)  # round四舍五入保留1位小数
  return area, len

c_area, c_len = circle_area_len(10)
print(c_area, c_len)

all = circle_area_len(10)
print(all[0])
print(all[1])



num = 100
def fun():
  num = 10000
  print('fun===', num)

fun()

print('global===', num)

# global 主要用在程序的配置、状态和计数器场景下
debug_mode = False

def enable_debug():
  global debug_mode
  debug_mode = True
  print('调试模式已开启')

def disable_debug():
  global debug_mode
  debug_mode = False
  print('调试模式已关闭')