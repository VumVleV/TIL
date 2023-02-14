import heapq
a = list(map(int,input().split()))
heapq.heapify(a)
heapq.heappop(a)
print(heapq.heappop(a))