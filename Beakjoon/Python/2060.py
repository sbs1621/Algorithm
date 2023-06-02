n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

count = 0

def dfs(node):
    visited[node] = True
    for i in graph[node]:
        if visited[i] == False:
            dfs(i)

dfs(1)

for i in range(2, len(visited)):
    if visited[i] == True:
        count += 1

print(count)
