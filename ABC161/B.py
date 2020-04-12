# coding: utf-8
from decimal import Decimal

# 標準入力 <int><int>
N, M = map(int, input().split())

# 標準入力 <int> list[]
n = list(map(int, input().split()))

n = sorted(n)
sosu = Decimal(str(sum(n)))
toku = Decimal("1") / Decimal(str((4 * M)))
border = sosu * toku

if n[M * -1] < border:
  print("No")
else:
  print("Yes")
