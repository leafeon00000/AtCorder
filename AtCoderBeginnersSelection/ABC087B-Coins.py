# coding: utf-8

# 標準入力 <int>
A = int(input())  # 500円玉
B = int(input())  # 100円玉
C = int(input())  # 50円玉
X = int(input())  # 目的金額

ans = 0

for _A in range(A + 1):
    if 500 * _A == X:
        ans += 1
    else:
        for _B in range(B + 1):
            if (500 * _A) + (100 * _B) == X:
                ans += 1
            else:
                for _C in range(C + 1):
                    if (500 * _A) + (100 * _B) + (50 * _C) == X:
                        ans += 1

print(ans)
