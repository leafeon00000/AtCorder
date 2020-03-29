# coding: utf-8

# 標準入力 <int><int>
X, Y, A, B, C = map(int, input().split())

# 標準入力 <int> list[]
p = sorted([int(i) for i in input().split()])
q = sorted([int(i) for i in input().split()])
r = sorted([int(i) for i in input().split()])

l = p[A - X:] + q[B - Y:] + r

print(sum(sorted(l)[(X+Y) * -1:]))
