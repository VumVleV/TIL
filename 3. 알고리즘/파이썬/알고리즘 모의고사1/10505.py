T = int(input())
for i in range(T):
    cnt = 0
    sum = 0
    blank = input()
    a = list(map(int, input().split()))
    for j in range(len(a)):
        sum += a[j]
    avg = sum/len(a)
    for k in range(len(a)):
        if a[k]<=avg:
            cnt+=1
    print(f"#{i+1} {cnt}")