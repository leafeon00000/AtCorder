# coding: utf-8

# 標準入力 <int><int>
N, P = map(int, input().split())

# 標準入力<str>
S = input()

ans = 0

for _n in range(N):
    for _n2 in range(_n + 1, N + 1):
        if int(S[_n:_n2]) % P == 0:
            ans += 1

print(ans)
