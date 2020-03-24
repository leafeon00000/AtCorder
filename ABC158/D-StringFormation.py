# coding: utf-8

# 標準入力 <int>
S = str(input())
Q = int(input())

# 標準入力 <str> list[][] 複数行・複数列
Qv = []
for _ in range(Q):
    Qv.append(list(map(str, input().split())))

for _ in range(Q):
    if Qv[_][0] == "1":
        S = S[::-1]
    elif Qv[_][0] == "2":
        if Qv[_][1] == "1":
            S = Qv[_][2] + S
        elif Qv[_][1] == "2":
            S = S + Qv[_][2]

print(S)
