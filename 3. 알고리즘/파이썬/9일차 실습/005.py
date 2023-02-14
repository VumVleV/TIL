o = int(input())
a = o
cnt = 0
while True:
    b = a//10 + a%10
    a = a%10*10 + b%10
    cnt += 1
    if a == o:
        print(cnt)
        break