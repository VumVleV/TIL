a = int(input())
switch = 0
for i in range(a,0,-1):
    cnt = 0
    for j in range(len(str(i))):
        if cnt == 0 and ((str(i))[j] == '4' or (str(i))[j] == '7'):
            switch = 1
        else:
            cnt = 1
            switch = 0
    if switch == 1:
        print(i)
        break
