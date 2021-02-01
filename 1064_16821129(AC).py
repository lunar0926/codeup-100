a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
min = 0
if a < b:
    min = a
else: 
    min = b 
    
if min < c:
    min = min
else: 
    min = c
print(min)


