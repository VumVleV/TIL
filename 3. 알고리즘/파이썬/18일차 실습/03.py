def swap(arr1, arr2, arr3):
    for elem in arr3:
        if elem in arr2:
            arr2.remove(elem)
            swap(arr1, arr2, arr1[elem])
        else:
            pass


N = int(input())
arr1 = [[] for i in range(N)]
T = int(input())
for i in range(T):
    a, b = map(int,input().split())
    arr1[a-1].append(b-1)
    arr1[b-1].append(a-1)
cnt = len(arr1[0])
arr2 = [i+1 for i in range(N-1)]
swap(arr1,arr2,arr1[0])
print(N-len(arr2)-1)
