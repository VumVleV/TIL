a = input("이름을 입력하세요 ")
b = input("전화번호를 입력하세요 ")
c = input("거주지를 입력하세요 ")
dict_A = {
    "이름": a,
    "전화번호": b,
    "거주지": c,
}

print(dict_A)
for key, value in dict_A.items():
    print(key, value, sep = " : ") 
