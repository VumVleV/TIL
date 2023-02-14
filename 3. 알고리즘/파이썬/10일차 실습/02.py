T = int(input())
for i in range(T):
    a = input().split()
    for j in range(len(a)):
        print(a[j][::-1],end=' ')