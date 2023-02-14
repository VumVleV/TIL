a = input()
print(a[0:a.find('(')].count('@'), a[a.find(')'):].count('@'))