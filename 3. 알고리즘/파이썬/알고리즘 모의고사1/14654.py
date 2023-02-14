L = {3,4,5,6,9}
T = int(input())
for i in range(T):
    a = input()
    if len(a)-a.count('-')==16 and int(a[0]) in L:
        print(f"#{i+1} 1")
    else:
        print(f"#{i+1} 0")