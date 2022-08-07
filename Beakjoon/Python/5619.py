n = int(input())
data = []
for _ in range(n):
    d = int(input())
    data.append(d)
data.sort()

result = []
for i in data[:4]:
    for j in data[:4]:
        if i != j:
            r = int(str(i) + str(j))
            result.append(r)
result.sort()

print(result[2])