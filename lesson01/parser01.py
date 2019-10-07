#endcoding=utf8

def grammar_parser(gram_str: str, stmt_split: str = '=', or_split: str = '|') -> dict:
    grammar = {}
    for line in gram_str.split('\n'):
        if not line.strip(): continue
        stmt, expr = line.split(stmt_split)
        grammar[stmt.strip()] = [i.strip() for i in expr.split(or_split)]
    return grammar

import random
def generator(grammar: dict, target: str) -> str:
    target = target.strip()
    if target not in grammar:
        return target
    else:
        choice = random.choice(grammar[target])
        return ''.join(generator(grammar, c.strip()) for c in choice.split())

def generate(gram_str:str, target: str, stmt_split: str = '=', or_split: str = '|') -> str:
    grammar = grammar_parser(gram_str, stmt_split, or_split)
    return generator(grammar, target)

def generate_n(gram_str:str, target: str, n: int = 5, stmt_split: str = '=', or_split: str = '|') -> list:
    assert n >= 1
    return [generate(gram_str, target, stmt_split, or_split) for i in range(n)]

host = """
host = 寒暄 报数 询问 业务相关 结尾 
报数 = 我是 数字 号 ,
数字 = 单个数字 | 数字 单个数字 
单个数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
寒暄 = 称谓 打招呼 | 打招呼
称谓 = 人称 ,
人称 = 先生 | 女士 | 小朋友
打招呼 = 你好 | 您好 
询问 = 请问你要 | 您需要
业务相关 = 玩玩 具体业务
玩玩 = 耍一耍 | 玩一玩
具体业务 = 喝酒 | 打牌 | 打猎 | 赌博
结尾 = 吗？"""

holiday_gram = """
    句子 = 谁们 日子 干什么 语气
    谁们 = 谁 和 人们
    谁 = 你 | 我 | 他 | 他们 | 我们 | 你们
    人们 = 人们 、 人名 | 人名
    人名 = 老张 | 老魏 | 老杨 | 老朱
    日子 = 动词想 在 节日
    动词想 = 计划 | 打算 | 商量
    节日 = 国庆节 | 清明节 | 中秋节 | 元旦节
    干什么 = 打牌 | 逛街 | 登山  
    语气 = ？ | ！ | 吗？
"""

introduce_gram = """
    sentence = 景区介绍 ， 疑问句
    景区介绍 = 景区 介绍
    景区 = 黄山 | 西湖 | 华山 | 青城山
    介绍 = 是什么 | 是什么 ， 有什么
    是什么 = 是 一个 形容词 地方
    形容词 = 美丽滴 | 迷人的 | 优美的 | 糟糕的 
    有什么 = 有什么 ， 有 数量词 形容词 名词 | 有 数量词 形容词 名词
    数量词 = 数词 量词
    数词 = 很多 | 一 | 二 | 三
    量词 = 条 | 头 | 个 
    名词 = 猪 | 蛇妖 | 孔雀 | 鲤鱼
    疑问句 = 你 确认词 语气助词
    确认词 = 确定 | 认真的 | 骗人的 | 搞笑 | 信
    语气助词 = 吧？ | 吗？ | ？
"""

print(generate(host, 'host'))
print(generate_n(host, 'host', 3))
print(generate(holiday_gram, '句子'))
print(generate(introduce_gram, 'sentence'))


