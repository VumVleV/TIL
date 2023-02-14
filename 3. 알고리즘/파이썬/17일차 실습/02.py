w = []
k = []
for _ in range(10):
    w.append(int(input()))
w = sorted(w,reverse=True)
for _ in range(10):
    k.append(int(input()))
k = sorted(k,reverse=True)
print(w[0]+w[1]+w[2], k[0]+k[1]+k[2])
