a = input().split()
dict_a = {}
count = 0
for char in a:
    dict_a[char] = 0
for char in a:
    dict_a[char] += 1
for k, v in dict_a.items():
    print(k, v)

