a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
b = input()
cnt=0
for i in range(len(a)):
    if a[i] in b:
        cnt += b.count(a[i])
        b = b.replace(a[i],' ')
b = b.replace(' ','')
print(len(b)+cnt)