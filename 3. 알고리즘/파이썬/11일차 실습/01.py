cnt=0
c=[]
for i in range(7):
    a = int(input())
    if a%2==1:
        cnt+=a
        c.append(a)
c.sort()
if cnt==0:
    print(-1)
else:
    print(cnt)
    print(c[0])
    
        