a= []
a = list(map(int,input().split()))
b = sorted(a)
while a!=b:
    for i in range(len(a)-1):
        if(a[i]>a[i+1]):
            c = a[i]
            a[i] = a[i+1]
            a[i+1] = c
            for j in range(len(a)):
                print(a[j],end=' ')
            print("\n",end='')
