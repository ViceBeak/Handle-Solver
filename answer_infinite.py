import json
import random


class Idiom:
    def __init__(self, _dict):
        self.shengmu = _dict["shengmu"]
        self.yunmu = _dict["yunmu"]
        self.shengdiao = _dict["shengdiao"]


def count_best(idioms):
    words_count = {}
    for expression in idioms:
        word_shown = {}
        for word in expression:
            if not words_count.get(word):
                words_count[word] = 0
            if not word_shown.get(word):
                words_count[word] += 1
                word_shown[word] = True

    words_count = list(words_count.items())
    words_count.sort(key=lambda x: x[1], reverse=True)
    print("最高频率字为：")
    print(words_count[:max(len(words_count), 10)])
    print(f"目前词语还有{len(idioms)}个：")
    list_idioms = list(idioms)
    random.shuffle(list_idioms)
    best_idioms = [i for i in list_idioms if words_count[0][0] in i]
    if len(best_idioms) < 10:
        print(list_idioms)
    else:
        print(best_idioms[:max(len(best_idioms), 20)])
    print("\n")


if __name__ == "__main__":
    idioms = {}
    with open("data_infinite/answers_infinite_extra_noted.json", "r") as dataset:
        raw_idioms = json.load(dataset)

    for raw_idiom in raw_idioms:
        idioms[raw_idiom] = Idiom(raw_idioms[raw_idiom])

    for i in idioms:
        if len(idioms[i].shengmu) != 4:
            print(i)

    while len(idioms) != 1:
        count_best(idioms)

        for character in range(4):
            while True:
                print(f"第{character + 1}个字是？这个字（正确1，存在但位置不正确2，不存在3）")
                character_status = input().split(" ")
                if len(character_status) == 2:
                    break

            if character_status[1] == "1":
                for idiom in list(idioms.keys()):
                    if idiom[character] != character_status[0]:
                        idioms.pop(idiom)
            elif character_status[1] == "2":
                for idiom in list(idioms.keys()):
                    if (idiom[character] == character_status[0]) or (character_status[0] not in idiom):
                        idioms.pop(idiom)
            else:
                for idiom in list(idioms.keys()):
                    if character_status[0] in idiom:
                        idioms.pop(idiom)

            count_best(idioms)

            while True:
                print(f"第{character + 1}个字声母是？这个声母（正确1，存在但位置不正确2，不存在3）（如果无声母，建议输入5 3）")
                shengmu_status = input().split(" ")
                if len(shengmu_status) == 2:
                    break

            if shengmu_status[1] == "1":
                for idiom in list(idioms.keys()):
                    if idioms[idiom].shengmu[character] != shengmu_status[0]:
                        idioms.pop(idiom)
            elif shengmu_status[1] == "2":
                for idiom in list(idioms.keys()):
                    if (idioms[idiom].shengmu[character] == shengmu_status[0]) or (
                            shengmu_status[0] not in idioms[idiom].shengmu):
                        idioms.pop(idiom)
            else:
                for idiom in list(idioms.keys()):
                    if shengmu_status[0] in idioms[idiom].shengmu:
                        idioms.pop(idiom)

            count_best(idioms)

            while True:
                print(f"第{character + 1}个字韵母是？这个韵母（正确1，存在但位置不正确2，不存在3）")
                yunmu_status = input().split(" ")
                if len(yunmu_status) == 2:
                    break

            if yunmu_status[1] == "1":
                for idiom in list(idioms.keys()):
                    if idioms[idiom].yunmu[character] != yunmu_status[0]:
                        idioms.pop(idiom)
            elif yunmu_status[1] == "2":
                for idiom in list(idioms.keys()):
                    if (idioms[idiom].yunmu[character] == yunmu_status[0]) or (
                            yunmu_status[0] not in idioms[idiom].yunmu):
                        idioms.pop(idiom)
            else:
                for idiom in list(idioms.keys()):
                    if yunmu_status[0] in idioms[idiom].yunmu:
                        idioms.pop(idiom)

            count_best(idioms)

            while True:
                print(f"第{character + 1}个字声调是？这个声调（正确1，存在但位置不正确2，不存在3）")
                shengdiao_status = input().split(" ")
                if len(shengdiao_status) == 2:
                    break

            if shengdiao_status[1] == "1":
                for idiom in list(idioms.keys()):
                    if idioms[idiom].shengdiao[character] != shengdiao_status[0]:
                        idioms.pop(idiom)
            elif shengdiao_status[1] == "2":
                for idiom in list(idioms.keys()):
                    if (idioms[idiom].shengdiao[character] == shengdiao_status[0]) or (
                            shengdiao_status[0] not in idioms[idiom].shengdiao):
                        idioms.pop(idiom)
            else:
                for idiom in list(idioms.keys()):
                    if shengdiao_status[0] in idioms[idiom].shengdiao:
                        idioms.pop(idiom)

            count_best(idioms)

    print(f"答案是{idioms}")
