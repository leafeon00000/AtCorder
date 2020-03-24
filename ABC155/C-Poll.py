# coding: utf-8
import collections

n = int(input())
# 複数行標準入力
S = []
for _ in range(n):
    S.append(input())  # S += [input()] とも書ける

c = collections.Counter(S)
m = c.most_common()[0][1]
print("///////////////////////")
ans = []
for _c in c.items():
    if _c[1] == m:
        ans.append(_c[0])

for _ans in sorted(ans):
    print(_ans)
