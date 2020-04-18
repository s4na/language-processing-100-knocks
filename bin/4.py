# coding: utf-8

import re

# 04. 元素記号Permalink
# “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
# それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）
# への連想配列（辞書型もしくはマップ型）を作成せよ．

def extractionWord(i, word):
    NUMBERS = [1, 5, 6, 7, 8, 9, 15, 16, 19]

    if i in NUMBERS:
        return (word[0], i)
    else:
        return (word[:2],i)

def main():
    rawText = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    text = re.sub(r'[.|,]+', "", rawText)
    textList = text.split()
    
    hoge = enumerate(textList)
    print (hoge)
    
    result = [extractionWord(i, w) for i, w in hoge]

    return result

print(main())
