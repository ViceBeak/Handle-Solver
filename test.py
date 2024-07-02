import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("文本输入输出")

# 输入框
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# 输出标签
output_label = tk.Label(root, text="", width=50, height=4, bg="white", anchor="nw", justify="left")
output_label.pack(pady=10)

# 按钮点击事件处理函数
def display_text():
    input_text = entry.get()
    output_label.config(text=input_text)

# 确定按钮
button = tk.Button(root, text="确定", command=display_text)
button.pack(pady=10)

# 运行主循环
root.mainloop()
