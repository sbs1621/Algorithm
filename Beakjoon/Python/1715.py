import heapq

n = int(input())

data = []
for i in range(n):
    card = int(input())
    heapq.heappush(data, card)
result = 0

if len(data) == 1:
    print(0)
else:
    while len(data) > 1:
            add = heapq.heappop(data) + heapq.heappop(data)
            result += add
            heapq.heappush(data, add)
    print(result)