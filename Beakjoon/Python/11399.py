n = int(input())

data = list(map(int, input().split()))
data.sort()

count = 0
for i in range(n):
    count += sum(data[:i+1])

print(count)