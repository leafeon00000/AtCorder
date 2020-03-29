# coding: utf-8

import collections

# 標準入力 <int><int>
N, X, Y = map(int, input().split())

br = []

for i in range(N - 1):
  for j in range(i + 1, N):
    br.append(min(j - i, abs(X - (i + 1)) + 1 + abs(Y - (j + 1)), abs(Y - (i + 1)) + 1 + abs(X - (j + 1))))

c = collections.Counter(br)

for k, v in c.items():
  print(v)

for _ in range(N - 1 - len(c)):
  print(0)
