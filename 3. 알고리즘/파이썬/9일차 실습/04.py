a=[]
for i in range(9):
    a.append(int(input()))
b = sorted(a, reverse=True)
print(b[0])
cnt = 1
for j in range(9):
    if a[j]!=b[0]:
        cnt+=1
    else:
        break
print(cnt)