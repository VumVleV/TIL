T = int(input())
a = [char for char in input()]
cnt = 0
for i in range(len(a)):
    cnt+=int(a[i])
print(cnt)