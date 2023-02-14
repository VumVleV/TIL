T = int(input())
b = list(map(int,input().split()))
c = {}
cnt = 0
for i in range(len(b)):
    c[b[i]] = 0
for j in range(len(b)):
    c[b[i]] += 1
for k, v in c.items():
    if v != 1:
        cnt += (v-1)
print(cnt)