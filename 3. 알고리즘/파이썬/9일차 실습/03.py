T = int(input())
a=[]
for i in range(T):
    a.append(int(input()))
a.sort()
i=0
for i in range(T):
    print(a[i])