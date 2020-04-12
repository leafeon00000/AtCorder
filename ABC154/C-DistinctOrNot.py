# coding: utf-8
# 標準入力 <int>
N = int(input())
# 標準入力 <int> list[]
A = list(map(int, input().split()))

if (len(set(A)) == N):
    print("YES")
else:
    print("NO")
