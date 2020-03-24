# coding: utf-8
n = list(map(int, input().split()))
N, M = n[0], n[1]

# 複数行標準入力
I = []
for _ in range(M):
    I.append(list(map(str, input().split())))

ans = ['x'] * N

isOK = False

for j in range(M):
    if int(I[j][0]) > N:
        ans = "-1"
        break
    elif ans[int(I[j][0]) - 1] == str(I[j][1]) or ans[int(I[j][0]) - 1] == "x":
        ans[int(I[j][0]) - 1] = str(I[j][1])
    elif ans[int(I[j][0]) - 1] != str(I[j][1]):
        ans = "-1"
        break

if (ans[0] == "x" or ans[0] == "0") and ans != "-1":
    del ans[0]
    if ans[0] == "x" or ans[0] == "0":
        del ans[0]
        if ans[0] == "x":
            ans = "-1"
        elif ans[0] == "0":
            ans = "0"

if M == 0:
    ans = 0

print(int(''.join(ans).replace("x", "0")))
