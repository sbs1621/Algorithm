n, m = map(int, input().split())


result = 0;
for i in range(n):
    arrayData = list(map(int, input().split()))
    arrayData.sort()
    minValue = arrayData[0]
    result = max(result, minValue)

print(result)
