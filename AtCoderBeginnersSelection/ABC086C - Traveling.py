# coding: utf-8

# 標準入力 <int>
N = int(input())

# 標準入力 <int> list[][] 複数行・複数列
I = []
for _ in range(N):
    I.append(list(map(int, input().split())))

ans = "Yes"

for _n in range(N):
    t = I[_n][0]
    x = I[_n][1]
    y = I[_n][2]
    if not ((t - (x + y)) % 2 == 0 and t - (x + y) >= 0):
        ans = "No"
        break

print(ans)
