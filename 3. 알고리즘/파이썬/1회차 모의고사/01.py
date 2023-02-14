T = int(input())
cnt = 0
for i in range(T):
    a = list(map(int,input().split()))
    for j in range(len(a)):
        if(a[j]%2 != 0):
            cnt += a[j]
    print(f"#{i+1} {cnt}")
    cnt = 0