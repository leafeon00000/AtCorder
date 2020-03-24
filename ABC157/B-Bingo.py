# coding: utf-8
# ビンゴゲーム
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = list(map(int, input().split()))

N = int(input())
# 複数行標準入力
S = []
for _ in range(N):
    S.append(int(input()))  # S += [input()] とも書ける

for _S in S:
    for _l1 in range(len(l1)):
        if (_S == l1[_l1]):
            l1[_l1] = 0
    for _l2 in range(len(l2)):
        if (_S == l2[_l2]):
            l2[_l2] = 0
    for _l3 in range(len(l3)):
        if (_S == l3[_l3]):
            l3[_l3] = 0

isBingo = "No"
if (sum(l1) == 0 or sum(l2) == 0 or sum(l3) == 0 or l1[0] + l2[0] + l3[0] == 0 or l1[1] + l2[1] + l3[1] == 0 or l1[2] + l2[2] + l3[2] == 0 or l1[0] + l2[1] + l3[2] == 0 or l1[2] + l2[1] + l3[0] == 0):
    isBingo = "Yes"

print(isBingo)
