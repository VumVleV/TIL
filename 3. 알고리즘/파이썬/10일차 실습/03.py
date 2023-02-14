a = input()
cnt = 1
for j in range(len(a)//10+1):
    print(a[(cnt-1)*10:cnt*10])
    cnt+=1
