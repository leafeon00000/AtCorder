# coding: utf-8

# 標準入力<int>
N = int(input())

# 標準入力 <str> list[] 複数行
d = []
for _ in range(N):
    d.append(int(input()))

d.sort()
a = set(d)

print(len(a))
