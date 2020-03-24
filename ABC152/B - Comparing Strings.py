# coding: utf-8

# 標準入力 <int><int>
a, b = map(int, input().split())

A = ""
B = ""

for _a in range(a):
    A += str(b)
for _b in range(b):
    B += str(a)

d = [A, B]
d.sort()

print(d[0])
