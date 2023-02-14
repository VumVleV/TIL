number_list = [2, 3, 5, 7]

count = 0
for num in number_list:
    count += 1

sum = 0
for i in range(count):
    sum+=number_list[i]

avg = sum/count
print(avg)