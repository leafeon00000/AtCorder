L, R = map(int, input().split())
print(type(L), L, R)

if L < 10:
    print(R + (100*(10-L)))
else:
    print(R)
