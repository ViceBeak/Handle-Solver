import json
from pypinyin import pinyin

if __name__ == "__main__":
    idioms = {}

    with open("idioms.json", "r", encoding="utf-8") as dataset:
        raw_idioms = json.load(dataset)

    count = 0
    normal = 0
    noted = 0
    for raw_idiom in raw_idioms:
        shengmu = []
        yunmu = []
        shengdiao = []

        if len(raw_idiom) == 1:

            raw_idiom = raw_idiom[0]

            for index, _shengmu in enumerate(pinyin(raw_idiom, style=3)):
                if _shengmu[0]:
                    shengmu.append(_shengmu[0])
                elif pinyin(raw_idiom, style=4)[index][0] in ("y", "w"):
                    shengmu.append(pinyin(raw_idiom, style=4)[index][0])
                else:
                    shengmu.append(None)

            for index, _pinyin in enumerate(pinyin(raw_idiom, style=8)):
                if _pinyin[0][-1] in ("1", "2", "3", "4"):
                    shengdiao.append(_pinyin[0][-1])
                    _pinyin = _pinyin[0][:-1]
                else:
                    shengdiao.append(None)
                    _pinyin = _pinyin[0]

                if shengmu[index]:
                    _yunmu = _pinyin[len(shengmu[index]):]
                else:
                    _yunmu = _pinyin
                yunmu.append(_yunmu)

            normal += 1

        elif len(raw_idiom) == 2:
            raw_idiom, _pinyin = raw_idiom
            characters = _pinyin.split(" ")
            for character in characters:
                if character[-1] in ("1", "2", "3", "4"):
                    shengdiao.append(character[-1])
                    character_normal = character[:-1]
                else:
                    shengdiao.append(None)
                    character_normal = character

                if character_normal.startswith("ch") or character_normal.startswith("zh") or character_normal.startswith("sh"):
                    shengmu.append(character_normal[:2])
                    yunmu.append(character_normal[2:])
                elif character_normal.startswith("a") or character_normal.startswith("e") or character_normal.startswith("i") or character_normal.startswith("u") or character_normal.startswith("v"):
                    shengmu.append(None)
                    yunmu.append(character_normal)
                else:
                    shengmu.append(character_normal[0])
                    yunmu.append(character_normal[1:])

            noted += 1

        idioms[raw_idiom] = {"shengmu": shengmu, "yunmu": yunmu, "shengdiao": shengdiao}

        count += 1
    print("count: ", count)
    print("normal: ", normal)
    print("noted:", noted)

    with open("answers_infinite_noted.json", "w") as file:
        json.dump(idioms, file, ensure_ascii=False)


