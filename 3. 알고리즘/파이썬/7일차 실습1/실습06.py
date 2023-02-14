T = int(input())
for i in range(T):
    N = int(input())
    for j in range(N):
        a = list(map(int,input().split()))
        for k in range(len(a)):
            print(a[k],end=' ')



