# class EduManagement:
#     def run(self):
#         choice = input('清选择要执行的操作，输入1-6：')
#         match choice:
#             case '1': # 添加学生
#                 self.add_student()
#             case '2': # 修改学生
#                 self.update_student()
#             case '3': # 删除学生
#                 self.delete_student()
#             case '4':
#                 self.query_student()
#             case '5':
#                 self.list_student()
#             case '6':
#                 print('Bye ~')
#                 # break
#             case _: # 其他情况
#                 print('输入错误，请选择1-6之间的菜单功能！')

# if __name__ == '__main__':
#     print('内部测试')
#     edu = EduManagement()
#     edu.run()


# 异常处理
try:
    print('====================================')
    # print(my_name)
    # print(1 / 0)
    # print('ABC'[8])
    o = {'a': 12}
    print(o.b)
    print('====================================')
except NameError as e:
    print('名词不存在的错误', e)
except ZeroDivisionError as e:
    print('0不能做被除数错误', e)
except IndexError as e:
    print('获取索引错误', e)
except Exception as e:  # 捕获所有的异常
    print('程序运行出错，联系管理员', e)
finally:
    print('释放了')