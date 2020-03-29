# coding: utf-8

# 標準入力 <int><int>
K, N = map(int, input().split())

# 標準入力 <int> list[]
A = list(map(int, input().split()))

lmax = 0

for a in range(N):
  if a != N - 1:
    if A[a + 1] - A[a] > lmax:
      lmax = A[a + 1] - A[a]
  else:
    if A[0] + K - A[a] > lmax:
      lmax = A[0] + K - A[a]

print(K - lmax)
