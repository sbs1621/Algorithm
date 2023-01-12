n,m = map(int, input().split())

i = 0
while True:
    i += 1
    if n % m == 0:
        n /= m
    else:
        n -= 1
    
    if n == 1:
        break
print(i)