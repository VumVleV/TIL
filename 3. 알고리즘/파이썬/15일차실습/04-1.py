# 망한 코드, 1by1 케이스에서 무한루프가 돈다

def need_swap(arr):
    cnt_test = 0
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            cnt_test += 1
    if cnt_test == 1 and arr[len(arr)-1] == 1:
        return False
    else:
        return True
        
def swap(arr,k,cnt):
    for i in range(k-1):
        if arr[i] == 1 and arr[i+1] == 0:
            arr[i+1] = 1
            arr[i] = 0
            cnt += 1
    return cnt

a = int(input())
for i in range(a):
    b, c = map(int,input().split())
    d = [[0 for _ in range(c)] for _ in range(b)]
    for k in range(b):
        e = list(map(int,input().split()))
        for l in range(c):
            d[k][l] = e[l]
    
    swap_cnt = 0
    for m in range(c):
        f = []
        for n in range(b):
            f.append(d[n][m])
        while need_swap(f):
            swap_cnt = swap(f,len(f),swap_cnt)
    print(swap_cnt)