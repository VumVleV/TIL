T = int(input())
a=[]
for i in range(T):
    b = int(input())
    a = [int(x) for x in input().split()]
    cnt = 0
    for j in range(len(a)):
        cnt+=a[j]
    print(cnt)