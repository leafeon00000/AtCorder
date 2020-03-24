# coding: utf-8
# 標準入力 <int><int>
N, K = map(int, input().split())
# 標準入力 <int> list[]
H = list(map(int, input().split()))

H = sorted(H)
'''
ans = 0
if N > K:
    for i in range(K):
        H.pop(0)
    ans = sum(H)

print(ans)
'''
if K == 0:
    print(sum(H))
else:
    print(sum(H[:-K]))
