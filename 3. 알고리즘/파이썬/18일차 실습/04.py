def swap(arr1, arr2, arr3):
    for elem in arr3:
        if elem in arr2:
            arr2.remove(elem)
            swap(arr1, arr2, arr1[elem])
        else:
            pass

while True:
    cnt = 0
    a, b = map(int,input().split())
    c = [[] for _ in range(a*b)]
    stack = [i for i in range(a*b)]
    if a == 0 and b == 0:
        break
    else:
        arr1 = [[0 for _ in range(a+2)] for _ in range(b+2)]
        for i in range(b):
            arr2 = list(map(int,input().split()))
            for j in range(a):
                arr1[i+1][j+1] = arr2[j]
        for i in range(b):
            for j in range(a):
                if arr1[i+1][j+1] == 1:
                    if arr1[i][j] == 1:
                        c[a*i+j].append(a*(i-1)+j-1)
                    if arr1[i][j+1] == 1:
                        c[a*i+j].append(a*(i-1)+j)
                    if arr1[i][j+2] == 1:
                        c[a*i+j].append(a*(i-1)+j+1)
                    if arr1[i+1][j] == 1:
                        c[a*i+j].append(a*i+j-1)
                    if arr1[i+1][j+2] == 1:
                        c[a*i+j].append(a*i+j+1)
                    if arr1[i+2][j] == 1:
                        c[a*i+j].append(a*(i+1)+j-1)
                    if arr1[i+2][j+1] == 1:
                        c[a*i+j].append(a*(i+1)+j)
                    if arr1[i+2][j+2] == 1:
                        c[a*i+j].append(a*(i+1)+j+1)
        while stack != []:
            for elem in stack:
                swap(c,stack,c[elem])
                cnt += 1
                break
        print(cnt)