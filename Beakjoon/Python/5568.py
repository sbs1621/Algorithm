n = int(input())

m = 1000 - n
count = 0
while True:
    if m == 0:
        break
    if m >= 500:
        m -= 500
        count += 1
    elif m >= 100:
        m -= 100
        count += 1
    elif m >= 50:
        m -= 50
        count += 1
    elif m >= 10:
        m -= 10
        count += 1
    elif m >= 5:
        m -= 5
        count += 1
    else:
        m -= 1
        count += 1

print(count)