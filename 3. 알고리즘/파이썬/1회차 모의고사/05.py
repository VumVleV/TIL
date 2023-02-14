T = int(input())
for i in range(T):
    N = int(input())
    b=0
    j=0
    c=[]
    while True:
        b = N*(j+1)
        for k in range(10):
            if str(k) in str(b):
                if k not in c:
                    c.append(k)
        if ((0 in c) and (1 in c) and (2 in c) and (3 in c) and (4 in c) and (5 in c) and (6 in c) and (7 in c) and (8 in c) and (9 in c)):
            print(f"#{i+1} {(j+1)*N}")
            break
        j = j+1

