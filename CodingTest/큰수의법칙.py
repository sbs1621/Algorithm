n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0
for i in range(m):
    if (i+1) % k != 0:
        result += first
    else:
        result += second
print(result)
