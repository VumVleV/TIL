N = input()
l = len(N)
c= []
for i in range(1,l-1):
    for j in range(i+1,l):
        e = N[0:i]
        f = N[i:j]
        g = N[j:l]
        d = e[::-1]+f[::-1]+g[::-1]
        c.append(d)
c = sorted(c)
print(c[0])