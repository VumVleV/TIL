a = input()
b = int(a)
cnt = 0
for i in range(len(a)):
    if i != len(a)-1:
        cnt += b//(10**(len(a)-1-i)) - 10*(b//(10**(len(a)-i)))
    else:
        cnt += b%10
if b < 0:
    print(-1)
else: 
    print(cnt)