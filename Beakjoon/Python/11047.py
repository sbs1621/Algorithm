coin, money = map(int, input().split())

arrayData = []

for i in range(coin):
    arrayData.append(int(input()))

count = 0
node = coin-1

while True:
    if money == 0:
        break
    if money >= arrayData[node]:
        money -= arrayData[node]
        count += 1
    else :
        node -= 1
print(count)
    