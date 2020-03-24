# coding: utf-8

# 標準入力<str>
S = input()
N = len(S)
n = int((N - 1) / 2)
n2 = int((N - 1) / 2)
S2 = S[0:n2]
n3 = int((N+3)/2)
S3 = S[n3 -1:]

isNo1OK = True
isNo2OK = True
isNo3OK = True

for i in range(n):
  if S[i] != S[(i + 1) * -1]:
    isNo1OK = False

for j in range(len(S2)):
  if S2[j] != S2[(j + 1) * -1]:
    isNo2OK = False

for k in range(len(S3)):
  if S3[k] != S3[(k + 1) * -1]:
    isNo2OK = False

if isNo1OK and isNo2OK and isNo3OK:
  print("Yes")
else:
  print("No")
