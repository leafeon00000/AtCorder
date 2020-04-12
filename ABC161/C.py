# coding: utf-8
# 標準入力 <int><int>
N, K = map(int, input().split())

print(min((N % K), abs((((N // K) + 1) * K) - N)))
