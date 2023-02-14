T = int(input())
a = [int(x) for x in input().split()]
a.sort()
print(a[0],a[len(a)-1],sep=' ')