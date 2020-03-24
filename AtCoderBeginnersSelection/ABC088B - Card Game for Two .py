# coding: utf-8

# 標準入力 <int>
N = int(input())

# 標準入力 <int> list[]
a = list(map(int, input().split()))

a.sort()
a = a[::-1]

al = 0
bo = 0

for _N in range(N):
    if _N % 2 == 0:
        al += a[_N]
    else:
        bo += a[_N]

print(al - bo)
