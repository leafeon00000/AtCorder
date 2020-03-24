# coding: utf-8
# 標準入力 <int><int>
N, A, B = map(int, input().split())

shou = N // (A + B)
amari = N % (A + B)

ans = A * shou

if amari <= A:
    ans += amari
else:
    ans += A

print(ans)
