# coding: utf-8

# 標準入力 <int>
N = int(input())

# 標準入力<str>
S = input()

R = S.count("R")
G = S.count("G")
B = S.count("B")

cnt = 0

for i in range(N - 2):
  for j in range(i + 1, N - 1):
    k = i + ((j - i) * 2)
    print(i,j,k)
    if k < N:
      print("****")
      if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
        cnt += 1

print(R * G * B - cnt, R , G, B, cnt)
