# coding: utf-8

import math

# 標準入力 <int><int>
a, b, c = map(float, input().split())

ans = "No"

if math.sqrt(a) + math.sqrt(b) - math.sqrt(c) < 0:
    ans = "Yes"

print(ans)
