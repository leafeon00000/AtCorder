# coding: utf-8

S, T = map(str, input().split())
A, B = map(int, input().split())
U = str(input())

if U == S:
  A -= 1
elif U == T:
  B -= 1

print(A, B)
