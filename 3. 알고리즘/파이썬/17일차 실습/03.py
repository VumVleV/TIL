T = int(input())
b = list(map(int,input().split()))
c = [0]
accrue = 0
for i in range(T-1):
    if b[i+1] > b[i]:
        accrue += b[i+1]-b[i]
        if i == T-2:
            c.append(accrue)
    else:
        if accrue != 0:
            c.append(accrue)
        accrue = 0
c = sorted(c)
print(c.pop())