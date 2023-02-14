dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

if "거주지" not in dict_variable:
    dict_variable["거주지"] = "서울특별시"
    # 거주지가 dict_varaible의 key에 포함되지 않는다면 거주지 key에 서울특별시를 새로이 할당한다

print(dict_variable)
    # {'이름': '정우영', '생년월일': '19000101', '회사': '하이퍼그로스', '거주지': '서울특별시'}
    