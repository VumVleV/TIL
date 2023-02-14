import sys
arr = []
N = int(sys.stdin.readline())
for i in range(N):
    arr.append(sys.stdin.readline().split())
    arr[i].append(1)
for i in range(N-1):
    for j in range(i+1,N):
        if arr[i][0] > arr[j][0] and arr[i][1] >= arr[j][1]:
            arr[j][2] += 1
        elif arr[i][0] >= arr[j][0] and arr[i][1] > arr[j][1]:
            arr[j][2] += 1
        elif arr[i][0] < arr[j][0] and arr[i][1] <= arr[j][1]:
            arr[i][2] += 1
        elif arr[i][0] <= arr[j][0] and arr[i][1] < arr[j][1]:
            arr[i][2] += 1
        else:
            pass
for i in range(N):
    print(arr[i][2],end = ' ')