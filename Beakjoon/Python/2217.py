n = int(input())
data = []
for _ in range(n):
    m = int(input())
    data.append(m)
data.sort()
maxNum = []

for _ in range(n):
    maxNum.append(min(data) * n)
    if n == 0:
        break
    del data[0]
    n -= 1
    
    

print(max(maxNum))