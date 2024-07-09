import tkinter as tk
import json
from tkinter import ttk


class Idiom:
    def __init__(self, _dict):
        self.shengmu = _dict["shengmu"]
        self.yunmu = _dict["yunmu"]
        self.shengdiao = _dict["shengdiao"]


def read_dataset():
    global idioms
    with open("data/answers_noted.json", "r") as _dataset:
        idioms = json.load(_dataset)
    remains_label.config(text=f"剩余词语数量：{len(idioms)}")
    calculate_frequency()


def read_dataset_infinite():
    global idioms
    with open("data_infinite/answers_infinite_extra_noted.json", "r") as _dataset:
        idioms = json.load(_dataset)
    remains_label.config(text=f"剩余词语数量：{len(idioms)}")
    calculate_frequency()


def calculate_frequency():
    global idioms
    character_frequency = {}
    shengmu_frequency = {}
    yunmu_frequency = {}
    shengdiao_frequency = {}
    for idiom in idioms:
        for character in idiom:
            if character not in character_frequency:
                character_frequency[character] = 1 / len(idioms)
            else:
                character_frequency[character] += 1 / len(idioms)
        for shengmu in idioms[idiom]["shengmu"]:
            if not shengmu:
                shengmu = "无声母"
            if shengmu not in shengmu_frequency:
                shengmu_frequency[shengmu] = 1 / len(idioms)
            else:
                shengmu_frequency[shengmu] += 1 / len(idioms)
        for yunmu in idioms[idiom]["yunmu"]:
            if yunmu not in yunmu_frequency:
                yunmu_frequency[yunmu] = 1 / len(idioms)
            else:
                yunmu_frequency[yunmu] += 1 / len(idioms)
        for shengdiao in idioms[idiom]["shengdiao"]:
            if not shengdiao:
                shengdiao = "无声调"
            if shengdiao not in shengdiao_frequency:
                shengdiao_frequency[shengdiao] = 1 / len(idioms)
            else:
                shengdiao_frequency[shengdiao] += 1 / len(idioms)

    character_count = [(key, round(value, 4)) for key, value in character_frequency.items()]
    character_count.sort(key=lambda x: x[1], reverse=True)
    frequency_character.config(text=f"{character_count[:10]}")
    shengmu_count = [(key, round(value, 4)) for key, value in shengmu_frequency.items()]
    shengmu_count.sort(key=lambda x: x[1], reverse=True)
    frequency_shengmu.config(text=f"{shengmu_count[:10]}")
    yunmu_count = [(key, round(value, 4)) for key, value in yunmu_frequency.items()]
    yunmu_count.sort(key=lambda x: x[1], reverse=True)
    frequency_yunmu.config(text=f"{yunmu_count[:10]}")
    shengdiao_count = [(key, round(value, 4)) for key, value in shengdiao_frequency.items()]
    shengdiao_count.sort(key=lambda x: x[1], reverse=True)
    frequency_shengdiao.config(text=f"{shengdiao_count}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("汉兜求解器")
    style = ttk.Style()
    style.configure("Pixel.TEntry", height=50)

    # 默认模式为标准模式
    with open("data/answers_noted.json", "r") as dataset:
        idioms = json.load(dataset)

    # 菜单，选择游戏模式
    menubar = tk.Menu(root)
    mode = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="游戏模式", menu=mode)
    mode.add_command(label="标准版", command=read_dataset)
    mode.add_command(label="无限版", command=read_dataset_infinite)

    # 第一部分（线索输入）框架
    first_frame = tk.Frame(root, bd=2, relief="groove")
    first_frame.grid(row=0, column=0, padx=10, pady=10)

    # 4个线索名称
    clue_label_frame = tk.Frame(first_frame)
    clue_label_frame.grid()
    clue_labels = ["", "汉字", "声母", "韵母", "声调"]
    for i, clue in enumerate(clue_labels):
        tk.Label(clue_label_frame, text=clue).grid(row=i + 1, column=0)

    # 3种情况
    judge_labels = ["正确", "存在但位置错误", "不存在"]

    # 正确情况
    judge_frame_1 = tk.Frame(first_frame, bd=2, relief="groove")
    judge_frame_1.grid(row=0, column=1, padx=2, pady=2)
    tk.Label(judge_frame_1, text="正确").grid(row=0, columnspan=4, sticky="we")
    for i in range(4):
        for j in range(4):
            entry = ttk.Entry(judge_frame_1, width=4, style="Pixel.TEntry")
            entry.grid(row=i + 1, column=j)

    # 存在但位置错误情况
    judge_frame_2 = tk.Frame(first_frame, bd=2, relief="groove")
    judge_frame_2.grid(row=0, column=2, padx=2, pady=2)
    tk.Label(judge_frame_2, text="存在但位置错误").grid(row=0, columnspan=4, sticky="we")
    for i in range(4):
        for j in range(4):
            entry = ttk.Entry(judge_frame_2, width=10, style="Pixel.TEntry")
            entry.grid(row=i + 1, column=j)

    # 不存在
    judge_frame_3 = tk.Frame(first_frame, bd=2, relief="groove")
    judge_frame_3.grid(row=0, column=3, padx=2, pady=2)
    tk.Label(judge_frame_3, text="不存在").grid(row=0, columnspan=4, sticky="we")
    for i in range(4):
        entry = ttk.Entry(judge_frame_3, width=60, style="Pixel.TEntry")
        entry.grid(row=i + 1)

    # 第一部分的按钮框架
    first_button_frame = tk.Frame(first_frame)
    first_button_frame.grid(row=1, columnspan=4, padx=3, pady=3)

    # 第一部分的确定按钮
    first_confirm_button = tk.Button(first_button_frame, width=5, text="确定", relief="groove")
    first_confirm_button.grid(row=0, column=0, padx=3, pady=3)

    # 第一部分的重置按钮
    first_clear_button = tk.Button(first_button_frame, width=5, text="重置", relief="groove")
    first_clear_button.grid(row=0, column=1, padx=3, pady=3)

    # 第二部分（语素筛选）框架
    second_frame = tk.Frame(root, bd=2, relief="groove")
    second_frame.grid(row=1, column=0, padx=10)

    # 剩余词语框架
    remains_frame = tk.Frame(second_frame)
    remains_frame.grid(row=0, columnspan=3, padx=2, pady=2)

    remains_label = tk.Label(remains_frame, text=f"剩余词语数量：{len(idioms)}", font=("微软雅黑", 10))
    remains_label.grid()

    # 4个线索名称
    clue_label_frame = tk.Frame(second_frame)
    clue_label_frame.grid(row=1, column=0)
    clue_labels = ["", "汉字", "声母", "韵母", "声调"]
    for i, clue in enumerate(clue_labels):
        tk.Label(clue_label_frame, text=clue).grid(row=i + 1, column=0)

    # 语素频率框架
    frequency_frame = tk.Frame(second_frame, bd=2, relief="groove")
    frequency_frame.grid(row=1, column=1, padx=2, pady=2)
    tk.Label(frequency_frame, text="最高频率").grid(row=0, sticky="we")
    frequency_character = tk.Label(frequency_frame, text="", bg="white", width=118, bd=2, relief="groove")
    frequency_character.grid(row=1)
    frequency_shengmu = tk.Label(frequency_frame, text="", bg="white", width=118, bd=2, relief="groove")
    frequency_shengmu.grid(row=2)
    frequency_yunmu = tk.Label(frequency_frame, text="", bg="white", width=118, bd=2, relief="groove")
    frequency_yunmu.grid(row=3)
    frequency_shengdiao = tk.Label(frequency_frame, text="", bg="white", width=118, bd=2, relief="groove")
    frequency_shengdiao.grid(row=4)

    calculate_frequency()

    # 权重框架
    weight_frame = tk.Frame(second_frame, bd=2, relief="groove")
    weight_frame.grid(row=1, column=2, padx=2, pady=2)
    tk.Label(weight_frame, text="权重").grid(row=0, sticky="we")
    for i in range(4):
        entry = ttk.Entry(weight_frame, width=5, style="Pixel.TEntry")
        entry.grid(row=i + 1)

    # 第二部分的按钮框架
    second_button_frame = tk.Frame(second_frame)
    second_button_frame.grid(row=2, columnspan=3, padx=3, pady=3)

    # 第二部分的确定按钮
    second_confirm_button = tk.Button(second_button_frame, width=5, text="确定", relief="groove")
    second_confirm_button.grid(row=0, column=0, padx=3, pady=3)

    # 第三部分（推荐输出）框架
    third_frame = tk.Frame(root, bd=2, relief="groove")
    third_frame.grid(row=2, column=0, padx=10, pady=10)

    # 保守策略框架
    conservative_frame = tk.Frame(third_frame)
    conservative_frame.grid(row=0, column=0, padx=3, pady=3)

    tk.Label(conservative_frame, text="保守策略（不违反\n已知条件）").grid(row=0, column=0)
    tk.Label(conservative_frame, text="", bg="white", width=115, bd=2, relief="groove").grid(row=0, column=1)

    # 最大熵框架
    aggressive_frame = tk.Frame(third_frame)
    aggressive_frame.grid(row=1, column=0, padx=3, pady=3)

    tk.Label(aggressive_frame, text="最大熵（可能违反\n已知条件）").grid(row=0, column=0)
    tk.Label(aggressive_frame, text="", bg="white", width=115, bd=2, relief="groove").grid(row=0, column=1)

    root.config(menu=menubar)
    # 运行主循环
    root.mainloop()
