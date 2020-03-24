# coding: utf-8
# n本の花から花束を作る問題。ただしa本、b本はダメ。
# 処理が重すぎた

#####コンビネーション nCr #######
from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under
################################


N = list(map(int, input().split()))  # n a b
n, a, b = N[0], N[1], N[2]
w = 10 ** 9 + 7

taba = 0

for i in range(1, n + 1):
    if (i != a and i != b):
        taba += cmb(n, i)

print(taba % w)
