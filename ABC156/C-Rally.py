# coding: utf-8
n = int(input())
x = list(map(int, input().split()))

HPlist = []

for num in range(100):
    tmp = 0
    for pnum in x:
        tmp += (pnum - num) ** 2
    HPlist.append(tmp)

print(min(HPlist))
