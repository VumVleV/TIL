a=input("문자열을 입력하세요")
for i in range(len(a)):
    print(a[len(a)-i-1])

a=input("문자열을 입력하세요")
for num in a[::-1]:
    print(num)