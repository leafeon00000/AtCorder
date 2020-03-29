import math

N, K = map(int, input().split())

ketasuu = 1

while N >= K:
    N = math.floor(N / K)
    ketasuu += 1

print(ketasuu)
