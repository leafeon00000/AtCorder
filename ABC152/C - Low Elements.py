# coding: utf-8

# 標準入力 <int>
N = int(input())

# 標準入力 <int> list[]
P = list(map(int, input().split()))

count = 0
comp = 2 * (10**5)

for i in range(N):
    if comp >= P[i]:
        count += 1
        comp = P[i]

print(count)
