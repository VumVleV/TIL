a = {}
for i in range(10):
    b = int(input())
    if b in a.keys():
        a[b] += 1
    else:
        a[b] = 1
j = max(a.values())
cnt = 0
sum_1 = 0
sum_2 = 0
for k, v in a.items():
    sum_1 += k*v
    sum_2 += v
    if v == j and cnt ==0:
        kk = k
        cnt+=1
print(int(sum_1/sum_2))
print(kk)
