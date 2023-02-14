T = int(input())
for i in range(T):
    a = int(input())
    b = [25, 10, 5, 1]
    for k in b:
        print(a//k, end=' ')
        a -= (a//k)*k