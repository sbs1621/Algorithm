import heapq

n = int(input())
data = []

for i in range(n):
    start, end = map(int, input().split())
    data.append([start, end])
data.sort()

classRoom = []
heapq.heappush(classRoom, data[0][1])

for i in range(1, n):
    if data[i][0] < classRoom[0]:
        heapq.heappush(classRoom, data[i][1])
    else:
        heapq.heappop(classRoom)
        heapq.heappush(classRoom, data[i][1])
print(len(classRoom))