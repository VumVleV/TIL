a=int(input("정수를 입력하세요 "))
if(a<1):
    print(False)
for i in range(a):
    if(i%2!=0):
        print(i)
    else:
        continue
