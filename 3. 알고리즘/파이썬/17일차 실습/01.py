a = [1,0,0]
T = int(input())
for i in range(T):
    b, c = map(int,input().split())
    k = a[b-1]
    a[b-1] = a[c-1]
    a[c-1] = k
for j in range(3):
    if a[j] == 1:
        print(j+1)
