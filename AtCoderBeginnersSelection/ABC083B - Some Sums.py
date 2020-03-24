# coding: utf-8

# 標準入力 <int><int>
N, A, B = map(int, input().split())

l = []

for _N in range(N + 1):
    tmp = 0
    for _N2 in range(len(str(_N))):
        tmp += int(str(_N)[_N2])
    if A <= tmp and tmp <= B:
        l.append(_N)

print(sum(l))
