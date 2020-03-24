# coding: utf-8

# 標準入力 <int><int>
a, b = map(int, input().split())

if a * b % 2 == 0:
    print("Even")
else:
    print("Odd")
