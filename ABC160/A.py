# coding: utf-8

# 標準入力<str>
S = input()

ans = "Yes"

if S[2] != S[3]:
  ans = "No"

if S[4] != S[5]:
  ans = "No"

print(ans)
