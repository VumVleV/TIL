a, b = map(int,input().split())
c = list(map(int,input().split()))
d = list(map(int,input().split()))
e = set()
f = set()
for i in range(a):
    e.add(c[i])
for j in range(b):
    f.add(d[j])
g = e ^ f
print(len(g))