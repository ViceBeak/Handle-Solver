import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("输入框界面")

# 创建框架布局
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# 标签文本
labels = ["正确", "存在但位置错误", "不存在"]
sub_labels = ["汉字", "声母", "韵母", "声调"]

# 创建标签
for i, label in enumerate(labels):
    tk.Label(frame, text=label).grid(row=0, column=i*4+1)

for i, sub_label in enumerate(sub_labels):
    tk.Label(frame, text=sub_label).grid(row=i+1, column=0)
    tk.Label(frame, text=sub_label).grid(row=i+1, column=2)
    tk.Label(frame, text=sub_label).grid(row=i+1, column=4)

# 创建输入框
entries = []

for i in range(4):  # 行
    for j in range(3):  # 列
        row_entries = []
        for k in range(4):  # 每个单元格中的输入框数量
            entry = tk.Entry(frame, width=10)
            entry.grid(row=i+1, column=j*4+1+k, padx=2, pady=2)
            row_entries.append(entry)
        entries.append(row_entries)

# 确定按钮点击事件处理函数
def submit():
    # 获取输入框中的内容并打印（或执行其他操作）
    for row in entries:
        for entry in row:
            print(entry.get())

# 确定按钮
button = tk.Button(frame, text="确定", command=submit)
button.grid(row=5, column=2, columnspan=3, pady=10)

# 运行主循环
root.mainloop()
