a = input("이름을 입력하세요 ")
b = input("전화번호를 입력하세요 ")
c = input("이메일을 입력하세요 ")
d = input("거주지를 입력하세요 ")

dict_A = {
    '전화번호': b,
    '이메일': c,
    '거주지': d,
}

dict_B = {
    a: dict_A,
}

print(dict_B)