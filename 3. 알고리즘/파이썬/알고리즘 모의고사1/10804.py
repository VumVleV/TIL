T = int(input())
for i in range(T):
    a = input()
    b = a[::-1]
    b = b.replace('b','z')
    b = b.replace('p','x')
    b = b.replace('d','c')
    b = b.replace('q','v')
    b = b.replace('z','d')
    b = b.replace('x','q')
    b = b.replace('c','b')
    b = b.replace('v','p')
    print(f"#{i+1} {b}")