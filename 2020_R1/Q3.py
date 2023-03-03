l = 0
out = ""
for i in range(4):
  f = input()
  out += f
  if(i < 3):
    out += ', '
print(out)
print(len(out)*'-')
