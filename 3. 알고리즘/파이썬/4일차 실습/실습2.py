a = input("문자열을 입력하세요 ")
count = 0
for char in a:
    if any([char=='a', char=='e', char=='i', char=='o', char=='u']):
        count += 1

print(count) 
