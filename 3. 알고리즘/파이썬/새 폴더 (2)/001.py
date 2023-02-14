cnt = 0
a = []
for i in range(5):
    a.append(int(input()))
    if(a[i] < 40):
        cnt += 40
    else:
        cnt+=a[i]
print(int(cnt/5))