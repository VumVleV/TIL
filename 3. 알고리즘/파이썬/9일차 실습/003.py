c=[]
d=[]
for i in range(3):
    a, b = map(int,input().split())
    c.append(a)
    d.append(b)
if c.count(max(c))==1:
    a = max(c)
else:
    a = min(c)
if d.count(max(d))==1:
    b = max(d)
else:
    b = min(d)
print(a,b)