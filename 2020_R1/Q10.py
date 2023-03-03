s1 = int(input())
s2 = int(input())
track = input().split("_")[1:-1]
cnt = 0
for i in track:
    if len(i) > s1:
        break
    cnt += 1
    if cnt == s2:
        break

print(cnt)
