T = int(input())
for i in range(T):
    a = list(map(int,input().split()))
    b = sorted(a)
    b.pop()
    del b[0]
    if b[len(b)-1]-b[0] >= 4:
        print('KIN')
    else:
        print(sum(b))