import sys

N = int(sys.stdin.readline())
stack = []
cnt = 0
max = 0
for _ in range(N):
    stack.append(int(sys.stdin.readline()))
for i in range(N):
    pop = stack.pop()
    if pop > max:
        max = pop
        cnt += 1
print(cnt)