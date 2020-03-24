# coding: utf-8
# 標準入力 <int>
N = int(input())
# 標準入力 <int> list[]
A = list(map(int, input().split()))

"""
ans = "YES"
for _A1 in range(N):
    for _A2 in range(N):
        if _A1 != _A2:
            if A[_A1] == A[_A2]:
                ans = "NO"
                break
print(ans)
"""

if (len(set(A)) == N):
    print("YES")
else:
    print("NO")
