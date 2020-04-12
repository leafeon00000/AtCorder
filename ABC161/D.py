# coding: utf-8

# 標準入力 <int>
K = int(input())

if K < 10:
  print(K)
  exit()

cnt = 9

ind = [i for i in range(1,10)]
tmp = ind

while cnt <= K:
  l = []
  for i in range(len(tmp)):
    if tmp[i] % 10 == 0:
      #print(tmp[i], "a")
      l.append(tmp[i] * 10 + tmp[i] % 10)
      l.append(tmp[i] * 10 + tmp[i] % 10 + 1)
      cnt += 2
    elif tmp[i] % 10 == 9:
      #print(tmp[i], "b")
      l.append(tmp[i] * 10 + tmp[i] % 10 - 1)
      l.append(tmp[i] * 10 + tmp[i] % 10)
      cnt += 2
    else:
      #print(tmp[i], "c")
      l.append(tmp[i] * 10 + tmp[i] % 10 - 1)
      l.append(tmp[i] * 10 + tmp[i] % 10)
      l.append(tmp[i] * 10 + tmp[i] % 10 + 1)
      cnt += 3
  tmp = l
  ind += l

#print(ind)
print(ind[K-1])
