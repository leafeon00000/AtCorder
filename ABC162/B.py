# coding: utf-8

# 標準入力 <int>
N = int(input())

ans = 0

for i in range(N):
  if (i+1) % 3 != 0 and (i+1) % 5 != 0:
    ans += i + 1

print(ans)
