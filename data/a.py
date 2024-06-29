import json
from pypinyin import pinyin


if __name__ == "__main__":
    idioms = {}

    with open("answers_clean.txt", "r") as dataset:
        raw_idioms = dataset.readlines()

    for raw_idiom in raw_idioms:
        raw_idiom = raw_idiom.strip()
        shengmu = []
        yunmu = []
        shengdiao = []
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

        idioms[raw_idiom] = {"shengmu": shengmu, "yunmu": yunmu, "shengdiao": shengdiao}

    with open("answers_noted.json", "w") as file:
        json.dump(idioms, file, ensure_ascii=False)
