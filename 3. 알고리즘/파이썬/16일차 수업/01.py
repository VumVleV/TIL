a, b = map(int,input().split())
c = list(map(int,input().split()))
d={}
e={}
cnt = 0
for i in range(len(c)-2):
    for j in range(i+1,len(c)-1):
        for k in range(j+1,len(c)):
            cnt+=c[i]+c[j]+c[k]
            d[cnt] = 0
            cnt = 0
z = 10**9
for k, v in d.items():
    if b-k>=0 and b-k<=z:
        z= b-k
        y = k
print(y)

    