# 指定类型注解 —— 显示声明
a: int = 10
score: float = 90.5
hobby: str = '踢足球'
flag: bool = True
pic: None = None

names: list[str | int] = ['张三', '李四', '王五']
phones: set[str] = {'13800000000', '13900000000', '13800000000'}
options: dict[str, int] = {'size': 1, 'total': 10, 'pageNum': 3}
goods: tuple[str, int, int] = ('运动相机', 899, 2)


# 解释器会自动进行类型判断
nums = [1, 3, 5, 8]

# 默认参数何时创建；为何 `tags=[]` 可能串数据？
def add_tag(tag: str, tags: list[str] = []):
  tags.append(tag)
  return tags

tags = ['运动', '相机']
new_tags = add_tag('赚钱', tags)
print(new_tags)