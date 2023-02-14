alp = 'abcdefghijklmnopqrstuvwxyz'
b = input()
for i in range(len(alp)):
    if alp[i] in b:
        index = b.find(alp[i])
        print(index,end=' ')
    else:
        print(-1,end=' ')