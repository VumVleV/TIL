T = int(input())
a=[]
for i in range(T):
    b = int(input())
    if b ==0:
        a.pop()
    else:
        a.append(b)
cnt=0
for j in range(len(a)):
    cnt+=a[j]
print(cnt)
    