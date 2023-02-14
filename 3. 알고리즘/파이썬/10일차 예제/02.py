T = int(input())
c = ''
for i in range(T):
    a, b = input().split()
    for j in range(len(b)):
        c+=b[j]*int(a)
    print(c)
    c = ''
