# coding: utf-8
#from scipy.special import comb
import itertools
import math

n = 5
r = 2

# 階乗
math.factorial(n)

print(math.factorial(n))  # 5*4*3*2*1 = 120

# 順列 nPr = n!/(n-r)!
math.factorial(n) // math.factorial(n - r)

# リストから順列を生成
l = ['a', 'b', 'c', 'd']
p = itertools.permutations(l, 2)  # 2個ずつの組み合わせ。引数なしは全数
for v in p:
    print(v)

p_list = list(itertools.permutations(l, 2))
print(len(p_list), p_list)

# 組み合わせ nCr = n!/(r!*(n-r)!)
math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

print(math.factorial(n) // (math.factorial(n - r) * math.factorial(r)))

# 組み合わせ（SciPy）
#comb(r, n)

#print("comb", comb(r, n))
