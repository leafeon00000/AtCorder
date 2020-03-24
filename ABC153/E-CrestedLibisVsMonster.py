# coding: utf-8

# 標準入力 <int><int>
H, N = map(int, input().split())

# 標準入力 <int> list[][] 複数行・複数列
A = []
for _ in range(N):
    A.append(list(map(float, input().split())))
    




A = sorted(A)

print(A)
