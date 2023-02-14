T = int(input())
import queue
q = queue.Queue()
for i in range(T):
    q.put(i+1)
if T != 1:
    for j in range(T-1):
        print(q.get(),end=' ')
        c = q.get()
        q.put(c)
    print(c)
else:
    print(1)