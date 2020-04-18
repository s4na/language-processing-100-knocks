# coding: utf-8

import re

# 03. 円周率Permalink
# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

rawText = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# reオブジェクトは置換に正規表現が使える
text = re.sub(r'[.|,]+', "", rawText)
textList = text.split()
result = [len(w) for w in textList]
print(result)
