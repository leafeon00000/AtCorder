# coding: utf-8

import collections
import copy

# 標準入力 <int>
N = int(input())

# 標準入力 <str> list[]
A = list(map(str, input().split()))

c = collections.Counter(A)
nodel = 0

for cv in c.values():
  if cv >= 2:
    nodel += int((cv * (cv-1))/2)

for a in A:
  ans = copy.copy(nodel)
  if c.get(a) >= 3:
    ans = ans - int((c.get(a)*(c.get(a)-1))/2) + int(((c.get(a)-1)*(c.get(a)-2))/2)
  elif c.get(a) == 2:
    ans -= 1
  print(ans)
