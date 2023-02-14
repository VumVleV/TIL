N, x = map(int,input().split())
N = 0
a = list(map(int,input().split()))
b=[]
for i in range(len(a)):
    if a[i]<x:
        b.append(a[i])
for j in range(len(b)):
    print(b[j],end=' ')
    