# coding: utf-8

import math
from functools import reduce

# 標準入力 <int>
N = int(input())

def gcd(*numbers):
    return reduce(math.gcd, numbers)

ans = 0

for a in range(N):
  for b in range(N):
    for c in range(N):
      #print(gcd(a + 1, b + 1, c + 1))
      ans += gcd(a + 1, b + 1, c + 1)

print(ans)
