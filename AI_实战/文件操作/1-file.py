# 文件操作入门
# 日常我们操作文件时，基本分为三步操作：打开、读/写、关闭。

# 读文件
# 1.打开文件
f = open('resources/poem.txt', 'r', encoding='utf-8')

# 2. 读取文件
# content = f.read()  # 读取所有内容
# print(content)

content_list = f.readlines()
for line in content_list:
    print(line.strip()) # 去掉多余空格和\n换行


# 3. 关闭文件
f.close()


# 写文件
fw = open('resources/poem2.txt', 'w', encoding='utf-8')

# try:
#     # 写入文件内容
#     fw.write('静夜思(李白)\n\n')
#     fw.write('床前明月光，\n')
#     fw.write('疑是地上霜，\n')
#     fw.write('举头望明月，\n')
#     fw.write('低头思故乡。')
# finally:    # 即使程序报错也依然可释放文件资源
#     fw.close()

# 真实项目中的异常捕获用with ... as ...:
# 代码执行完毕后文件会自动关闭，写起来更加的简单（推荐）
with open('resources/poem3.txt', 'w', encoding='utf-8') as fw:
    fw.write('静夜思(李白)\n\n')
    fw.write('床前明月光，\n')
    fw.write('疑是地上霜，\n')
    fw.write('举头望明月，\n')
    fw.write('低头思故乡。')