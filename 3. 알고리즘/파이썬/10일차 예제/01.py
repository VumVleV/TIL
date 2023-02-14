a = ['C','A','M','B','R','I','D','G','E']
b = input()
c = ''
for i in range(len(b)):
    if b[i] not in a:
        c+=b[i]
print(c)