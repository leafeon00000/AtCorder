import math

N, K = map(int, input().split())
print(type(N), N, K)

ketasuu = 1

while N >= K:
    N = math.floor(N / K)
    ketasuu += 1
    print(N, K, ketasuu)

print(ketasuu)
