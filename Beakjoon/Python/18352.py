from collections import deque

n, m, k, x = map(int, input().split())

graph = [[]for _ in range(n + 1)]

for i in range(m):
    a ,b = (map(int, input().split()))
    graph[a].append(b)

b = [-1] * (n+1)
b[x] = 0

queue = deque([x])
while queue:
    now = queue.popleft()
    for next in graph[now]:
        if b[next] == -1:
            b[next] = b[now] + 1
            queue.append(next)

check = 0

for i in range(len(b)):
    if b[i] == k:
        print(i)
        check = 1
        
if check == 0:
    print(-1)