# coding: utf-8
n = int(input())
x = list(map(int, input().split()))

isOK = "APPROVED"

for n in x:
    if (n % 2 == 0):
        if (n % 3 != 0 and n % 5 != 0):
            isOK = "DENIED"

print(isOK)
