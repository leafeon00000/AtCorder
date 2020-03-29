L, R = map(int, input().split())

if L < 10:
    print(R + (100*(10-L)))
else:
    print(R)
