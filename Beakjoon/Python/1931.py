import heapq
n = int(input())

data = []
for i in range(n):
    start, end = map(int, input().split())
    data.append([end, start])
data.sort()
count = 1;
meeting  = data[0][0]
#meeting = []
#heapq.heappush(meeting, data[0][0])

for i in range(1, n):
    if data[i][1] >= meeting:
        #heapq.heappop(meeting)
        #heapq.heappush(meeting, data[i][0])
        meeting = data[i][0]
        count += 1
print(count)