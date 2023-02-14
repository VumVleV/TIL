from collections import deque
a = input()
aq = deque([1])
bq = deque([1])
cnt = 0
while True:
    a = input()
    if a == "문제":
        aq.append(1)
    elif a == "고무오리":
        if aq == bq:
            aq.append(1)
            aq.append(1)
        else:
            aq.pop()
    else:
        if aq == bq:
            print("고무오리야 사랑해")
            break
        else:
            print("힝구")
            break