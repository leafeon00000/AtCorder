# coding: utf-8
# 標準入力 <int><int>
H, N = map(int, input().split())
# 標準入力 <int> list[]
A = list(map(int, input().split()))

ans = "NO"

if (H <= sum(A)):
    ans = "YES"

print(ans)
