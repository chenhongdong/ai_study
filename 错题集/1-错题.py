# 1.在windows系统中，时间格式化中冒号:不能出现，属于非法字符
  # 换为 - . 等字符都可
  # import time
  # time.strftime('%Y-%m-%d_%H-%M-%S')  ✅️


# 2.streamlit run在启动的时候，当前在哪个目录里启动的，就表示根目录在哪里
  # 如果在Py_study目录下启动，那么resources文件夹必须在根目录下
  # 如果在AI_实战目录下启动，那么如果想访问resources目录就必须在AI_实战目录下创建该同名目录才行