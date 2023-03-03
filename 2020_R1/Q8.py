a = int(input())
b = int(input())
ans = 0
while(b != -1):
  if(b >= a):
    ans += 1
  b = int(input())
print(ans)
