# coding: utf-8

# 標準入力 <int>
N = int(input())

# 標準入力 <int> list[]
A = list(map(int, input().split()))

isEven = True

ans = 0

while isEven:
    ans += 1
    for _N in range(N):
        if (A[_N] % 2 == 0):
            A[_N] /= 2
        else:
            isEven = False
            break

print(ans - 1)
