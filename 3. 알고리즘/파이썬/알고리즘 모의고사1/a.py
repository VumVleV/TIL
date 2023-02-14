from random import randrange
c=[]
for i in range(1000):
    number = randrange(100)
    c.append(number)
for j in range(len(c)):
    print(c[j],end=' ')