n = int(input())

data = []
me = 0
for i in range(n):
    m = int(input())
    if i == 0:
        me = m
    else:
        data.append(m)
data.sort(reverse=True)

count = 0
if n == 1:
    print(0)
    exit()
elif me > data[0]:
    print(0)
    exit()
else:
    while True:
        if me > data[0]:
            break
        data[0] -= 1
        me += 1
        count += 1
        if data[0] < max(data):
            data.sort(reverse=True)

print(count)  