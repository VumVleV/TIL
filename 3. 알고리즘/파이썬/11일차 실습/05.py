a = []
cnt = 1
for i in range(3):
    a.append(int(input()))
    cnt *= a[i]
for j in range(10):
    print(str(cnt).count(str(j)))
