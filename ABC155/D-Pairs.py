# coding: utf-8
# N枚から２枚を選んだ積を小さい順に並び替えてK番目にくるものは何か
n = list(map(int, input().split()))  # N K
m = list(map(int, input().split()))  # A1 A2...AN

sekiList = []

for i1 in range(len(m)):
    for i2 in range(len(m)):
        if (i1 < i2):
            sekiList.append(m[i1] * m[i2])

sekiList = sorted(sekiList)

print(sekiList[n[1] - 1])
