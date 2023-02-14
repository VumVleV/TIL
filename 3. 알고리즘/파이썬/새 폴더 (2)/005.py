T = int(input())
T = 0
a = list(map(int,input().split()))
cnt = 0
acm = 1
for i in range(len(a)-1):
    if a[i] == 1:
        if a[i+1] == 1:
            if i==0:
                cnt+=1
                acm+=1
                cnt+=acm
            else:
                acm+=1
                cnt+=acm        
        else:
            if i==0:
                cnt+=1
                acm = 1
            else:
                acm = 1
    else:
        if a[i+1] == 0:
            acm = 1
        else:
            cnt += 1
print(cnt)