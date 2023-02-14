T = int(input())
for i in range(T):
    blank = input()
    b={}
    d=[]
    c= input().split()
    for char in c:
        b[int(char)]=0
    for char in c:
        b[int(char)]+=1
    e = max(b.values())
    for k, v in b.items():
        if v == e:
            d.append(k)
    f = max(d)
    if len(d) == 1:
        print(f"#{i+1} {d[0]}")
    else:
        print(f"#{i+1} {f}")