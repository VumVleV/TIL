a, b = map(int, input().split())
for i in range(a):
    for j in range(b):
        a = list(map(int, input().split()))
        for k in range(len(a)):
            print(a[k],end=' ')
