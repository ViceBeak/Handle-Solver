# 汉兜Handle求解器

**请不要运行a.py，否则会覆盖answers_noted.json中u->v的修改**

## 使用方法

运行answer.py(针对官方版)/answer_infinite.py(针对无限版)

根据输入提示，输入形如“(汉字/声母/韵母/声调) (1/2/3)”的筛选条件，1代表该猜测正确，2代表该猜测存在但位置错误，3代表该猜测不存在

**需要注意特殊情况，若猜测中存在重复的clue，需人工甄别，如下图**

![image-20240629190113538](https://raw.githubusercontent.com/ViceBeak/Handle-Solver/master/img/image-20240629190113538.png)

对第三个字而言，声调2看似属于“猜测不存在”的情况，但事实上声调2存在于第四个字，因此第三个字声调的输入应该为“2 2”

## Reference

[[汉兜 - 汉字 Wordle (antfu.me)](https://handle.antfu.me/)](https://handle.antfu.me/)

[[汉兜 - 汉字 Wordle (无限) (bqx619.com)](https://handle.bqx619.com/)](https://handle.bqx619.com/)

**请注意无限版的大多数j、q、x后的u不会变为v**