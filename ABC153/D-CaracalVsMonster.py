# coding: utf-8

import math

# 標準入力 <int>
H = int(input())

n = 0
while H >= 1:
    n += 1
    H = H // 2

print(2 ** n - 1)
