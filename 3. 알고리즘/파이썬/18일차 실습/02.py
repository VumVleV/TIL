cnt = 0
arr = []
for i in range(4):
    a, b = map(int,input().split())
    cnt-=a    
    cnt+=b
    arr.append(cnt)
arr = sorted(arr)
print(arr.pop())