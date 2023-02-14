A = input()
cnt1 = 0
cnt2 = 0
cnt1 = A.count(':-)')
cnt2 = A.count(':-(')
if cnt1 > cnt2:
    print('happy')
elif cnt1 < cnt2:
    print('sad')
elif cnt1 == 0 and cnt2 == 0:
    print('none')
else:
    print('unsure')