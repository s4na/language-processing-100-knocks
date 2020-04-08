# coding: utf-8

# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

s1 = u'パトカー'
s2 = u'タクシー'

s_length = max(len(s1), len(s2))

s3 = u''

for i in range(s_length):
    s3 += s1[i] + s2[i]

print(s3)
