import datetime
date = datetime.date.today()
year = int(date.strftime("%Y"))
a = input("이름을 입력해주세요 ")
b = int(input("태어난 년도를 입력해주세요"))
print("저의 이름은 "+ str(a) + "이고, 올해 나이는 " + str(year -b +1) + "세 입니다.")