from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)

dfs_result = []
bfs_result = []


def dfs(node):
    dfs_visited[node] = True
    dfs_result.append(node)
    for i in graph[node]:
        if not dfs_visited[i]:
            dfs(i)


def bfs(node):
    queue = deque([node])
    bfs_visited[node] = True
    while queue:
        now = queue.popleft()
        bfs_result.append(now)
        for i in graph[now]:
            if not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i] = True

dfs(v)
bfs(v)
print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))