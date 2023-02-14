from datetime import datetime
now = datetime.now()

dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}

print(now.year - int(dict_variable["생년"]) + 1)