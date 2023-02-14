T = int(input())
for i in range(T):
    b = [1]*50
    a = input()
    for char in a:
        if char == "(":
            b.append("1")
        else:
            b.pop()
    if b == [1]*50 and a!='':
        print("YES")
    else:
        print("NO")
