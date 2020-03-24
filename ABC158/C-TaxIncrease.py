# coding: utf-8

import math
import decimal

# 標準入力 <int><int>
A, B = map(int, input().split())

tax8 = decimal.Decimal('0.08')
tax10 = decimal.Decimal('0.1')

ans = -1

for i in range(1, 1100):
    if math.floor(i * tax8) == A and math.floor(i * tax10) == B:
        ans = i
        break

print(ans)
