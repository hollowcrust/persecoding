s = "wibble wobble wibble wobble jelly on the plate"
a = s.split(" ")
s1 = input()
k = int(input())
pos = a.index(s1)
for i in range(1,k+1):
  print(a[pos + i], end=" ")
