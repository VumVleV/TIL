T = int(input())
cnt = 0
for i in range(T):
    a  = input().split()
    for j in range(len(a)):
        cnt += int(a[j])
    print(f"#{i+1} {int(round(cnt/len(a), 0))}")
    cnt = 0
    