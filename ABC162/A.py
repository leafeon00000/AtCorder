# coding: utf-8

# 標準入力<str>
N = input()

ans = "No"

for n in range(3):
  if N[n - 1] == "7":
    ans = "Yes"

print(ans)
