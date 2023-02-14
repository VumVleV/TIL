arr = [['-' for x in range(15)] for y in range(5)]
for i in range(5):
    a = input()
    for j in range(len(a)):
        arr[i][j] = a[j]
for k in range(len(arr[0])):
    for l in range(len(arr)):
        if arr[l][k] != '-':
            print(arr[l][k], end='')
