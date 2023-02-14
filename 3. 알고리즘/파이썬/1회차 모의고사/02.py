T = int(input())
for z in range(T):
    a = input()
    b=0
    c=0
    d=0
    for i in range(4):
        b += int(a[i])*(10**(3-i))
    for j in range(2):
        c += int(a[4+j])*(10**(1-j))
    for k in range(2):
        d += int(a[6+k])*(10**(1-k))
    e2 = (c==2)
    e3 = (c==1 or c== 3 or c== 5 or c== 7 or c== 8 or c== 10 or c==12)
    e4 = (c==4 or c==6 or c==9 or c==11)
    e5 = (d>=1 and d<=31)
    e6 = (d>=1 and d<=28)
    e7 = (d>=1 and d<=30)
    e = (e3 and e5) or (e2 and e6) or (e4 and e7)
    f1 = (b<10 and b>=1)
    f2 = (b<100 and b>=10)
    f3 = (b<1000 and b>=100)
    f6 = (b>=1000)
    f4 = (c<10)
    f5 = (d<10)
    if f1:
        b1 = "000"+str(b)
    elif f2:
        b1 = "00"+str(b)
    elif f3:
        b1 = "0"+str(b)
    elif f6:
        b1 = str(b)

    if f4:
        c1 = "0"+str(c)
    else:
        c1 = str(c)

    if f5:
        d1 = "0"+str(d)
    else:
        d1 = str(d)

    if(e):
        print(f"#{z+1} {b1}/{c1}/{d1}")
    else:
        print(f"#{z+1} {-1}")