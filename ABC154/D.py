# coding: utf-8

import decimal

# 標準入力 <int><int>
N, K = map(int, input().split())

# 標準入力 <int> list[]
p = list(map(int, input().split()))

def kitaiti(r):
  return decimal.Decimal(str(sum(range(1,r + 1)))) / decimal.Decimal(str(r))

max = 0
n = 0

for i in range(0, N-K+1):
  if sum(p[i:i + K]) > max:
    print(i, p[i])
    max = sum(p[i:i+K])
    n = i

print(max, i)

#print(kitaiti(p[n]) + kitaiti(p[n + 1]) + kitaiti(p[n+2]))
