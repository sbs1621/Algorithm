n,m = map(int, input().split())
data = []

for _ in range(n):
    row = list(map(int, input().split()))
    data.append(min(row))

print(max(data))