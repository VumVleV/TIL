T = int(input())
for i in range(T):
    cnt=0
    a = input().split()
    for j in range(15):
        if (j+1)%2==1:
            cnt+=int(a[j])*2
        else:
            cnt+=int(a[j])
    e = int(10 - cnt%10)
    if e == 10:
        e = 0
    print(f"#{i+1} {e}")