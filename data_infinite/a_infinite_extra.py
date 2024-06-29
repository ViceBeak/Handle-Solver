import json
from pypinyin import pinyin

if __name__ == "__main__":
    with open("answers_infinite_noted.json", "r") as original:
        original_data = json.load(original)

    with open("simple_dict.json", "r", encoding="utf-8") as extra:
        extra_data = json.load(extra)

    idioms = {}

    for extra_idiom in extra_data:
        extra_i = extra_idiom[0]
        if extra_i not in original_data:
            shengmu = []
            yunmu = []
            shengdiao = []

            for index, _shengmu in enumerate(pinyin(extra_i, style=3)):
                if _shengmu[0]:
                    shengmu.append(_shengmu[0])
                elif pinyin(extra_i, style=4)[index][0] in ("y", "w"):
                    shengmu.append(pinyin(extra_i, style=4)[index][0])
                else:
                    shengmu.append(None)

            for index, _pinyin in enumerate(pinyin(extra_i, style=8)):
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

            idioms[extra_i] = {"shengmu": shengmu, "yunmu": yunmu, "shengdiao": shengdiao}

    original_data.update(idioms)

    with open("answers_infinite_extra_noted.json", "w") as file:
        json.dump(original_data, file, ensure_ascii=False)