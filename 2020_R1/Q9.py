a = int(input())
b = int(input())
c = a

while(b and c >= 2 and c > 0.5 * a):
    b -= 1
    c -= 2
    
while(b*c):
    b -= 1
    c -= 1
    
print(c)
