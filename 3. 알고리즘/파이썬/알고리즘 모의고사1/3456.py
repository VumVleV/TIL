T = int(input())
for i in range(T):
    a, b, c = map(int,input().split())
    if a==b:
        print(f"#{i+1} {c}")
    else:
        print(f"#{i+1} {int((a**2+b**2-c**2)**(1/2))}")