# coding: utf-8

# 標準入力<str>
n = input()

# 標準入力 <int>
n = int(input())

# 標準入力 <int><int>
N, K = map(int, input().split())

# 標準入力 <str> list[]
n = list(map(str, input().split()))

# 標準入力 <str> list[]
n = list(map(str, input().split()))

# 標準入力 <int> list[]
n = list(map(int, input().split()))

# 標準入力 <str> list[] 複数行
S = []
for _ in range(n):
    S.append(input())  # S += [input()] とも書ける

# 標準入力 <str> list[][] 複数行・複数列
I = []
for _ in range(n):
    I.append(list(map(str, input().split())))

# 標準入力 <int> list[][] 複数行・複数列
I = []
for _ in range(n):
    I.append(list(map(int, input().split())))
