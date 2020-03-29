# coding: utf-8

import math

# 標準入力 <int><int>
n, a, b = map(int, input().split())

w = 10 ** 9 + 7

# 組み合わせ nCr = n!/(r!*(n-r)!)
def comb(n, r):
  return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

ans = ((2 ** n) - 1) -comb(n,a) - comb(n,b)

print(ans % w)
