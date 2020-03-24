# coding: utf-8

from decimal import Decimal

# 標準入力<str>
L = input()

LD = Decimal(L)
LD = LD/3

ans = LD ** 3

print(ans)
