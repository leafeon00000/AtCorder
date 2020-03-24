# coding: utf-8

# 標準入力 <int><int>
N, Y = map(int, input().split())

ans = [-1, -1, -1]

for _N1 in range(N + 1):
    for _N2 in range(N - _N1 + 1):
        _N3 = N - _N1 - _N2
        #print(_N1, _N2, _N3)
        if (Y == (10000 * _N1) + (5000 * _N2) + (1000 * _N3)):
            ans = [_N1, _N2, _N3]

print(ans[0], ans[1], ans[2])
