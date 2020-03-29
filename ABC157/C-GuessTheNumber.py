# coding: utf-8
n = list(map(int, input().split()))
N, M = n[0], n[1]

# 複数行標準入力
I = []
for _ in range(M):
    I.append(list(map(str, input().split())))

ans = -1

for i in I:
    if i[1] == '0':
        if int(i[0]) < N:
            print(ans)
            exit()

for a in range(1000):
    sn = str(a).zfill(3)
    isOk = True
    #print("++++", a)
    for i in range(M):
        #print(I[i][0], sn[int(I[i][0]) - 1], I[i][1])
        if sn[int(I[i][0]) - 1] != I[i][1]:
            isOk = False
            break
    if isOk:
        ans = a
        break

print(int(ans))
