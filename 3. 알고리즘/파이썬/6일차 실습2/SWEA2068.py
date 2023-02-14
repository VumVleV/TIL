T = int(input())
for i in range(T):
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(f"#{i+1} {a[0]}")