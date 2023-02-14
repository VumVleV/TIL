d=[]
for i in range(int(input())):
    b, c = input().split()
    if c == 'enter':
        d.append(b)
    elif b in d:
        d.remove(b)
d.sort(reverse=True)
for char in d:
    print(char)