n, m = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
count = 0
r = []

for j in range(n):
    if data[j] % 10 == 0:
        if data[j] // 10 <= m + 1:
            count += data[j] // 10
            m -= (data[j] // 10) - 1
        else:
            count += m
            print(count)
            exit() 
    else:
        r.append(data[j])

while len(r) != 0 and m != 0:
    result = r[0] // 10
    if result <= m + 1:
        count += result
        m -= result
        del(r[0])
    else:
        count += m
        break

print(count)