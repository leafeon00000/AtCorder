# coding: utf-8

# 標準入力<str>
S = input()

strList = ["dream", "dreamer", "erase", "eraser"]

while len(S) > 0:
    if S[-5:] == "dream" or S[-5:] == "erase":
        S = S[:-5]
    elif S[-6:] == "eraser":
        S = S[:-6]
    elif S[-7:] == "dreamer":
        S = S[:-7]
    else:
        break

if len(S) == 0:
    print("YES")
else:
    print("NO")
