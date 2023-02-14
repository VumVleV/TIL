a = input('문자열을 입력하세요 ')
dict_A = {}
for char in a:
    dict_A[char] = 0
for char in a:
    dict_A[char] += 1
for key, value in dict_A.items():
    print(key, value)

# 딕셔너리의 키는 유일성을 보장한다!