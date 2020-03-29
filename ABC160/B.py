# coding: utf-8

# 標準入力 <int>
X = int(input())

Y500 = 0
Y5 = 0

Y500 = X // 500

x = X % 500

Y5 = x // 5

print((Y500 * 1000) + (Y5 * 5))
