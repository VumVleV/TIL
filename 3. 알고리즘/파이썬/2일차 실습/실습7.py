a=int(input("첫 번째 정수를 입력하세요"))
b=int(input("두 번째 정수를 입력하세요"))
c=min(a,b) 
d=max(a,b)
if(a==b):
    print(False)
for i in range(c+1, d):
    print(i,end=" ")