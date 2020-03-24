# coding: utf-8
x = list(map(int, input().split()))

sameNum = 0
diffNum = 0

for n in x:
    for m in x:
        if n == m:
            sameNum += 1
        else:
            diffNum += 1

if sameNum == 5:
    print("Yes")
else:
    print("No")
