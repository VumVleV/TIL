s = set()
for i in range(4):
    a, b, c, d = map(int,input().split())
    for j in range(a,c):
        for k in range(b,d):
            s.add(tuple[j,k])
print(len(s))