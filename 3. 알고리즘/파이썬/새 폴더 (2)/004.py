cute = {}
cute['O'] = 0
cute['N'] = 0

T = int(input())
for i in range(T):
    if int(input()) == 1:
        cute['O'] += 1
    else:
        cute['N'] += 1

if cute['O'] > cute['N']:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")


