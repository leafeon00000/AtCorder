# coding: utf-8

# 標準入力 <int><int>
H, W = map(int, input().split())

ans = H * W // 2

if (H * W) % 2 == 1:
    ans += 1

if H == 1 or W == 1:
    ans = 1

print(ans)
