a = {
    1 : [],
    2 : ['A','B','C'],
    3 : ['D','E','F'],
    4 : ['G','H','I'],
    5 : ['J','K','L'],
    6 : ['M','N','O'],
    7 : ['P','Q','R','S'],
    8 : ['T','U','V'],
    9 : ['W','X','Y','Z'],
    0 : [],
}
cnt = 0
b = input()
for key in a:
    for i in range(len(b)):
        if b[i] in a[key]:
            cnt += key+1
print(cnt)