n = int(input())

five = 0
one = 0
ten = 0

while True:
    if n % 10 != 0 or n <= 0:
        break
    if n - 300 >= 0:
        n -= 300
        five += 1
    elif n - 60 >= 0:
        n -= 60
        one += 1
    elif n - 10 >= 0:
        n -= 10
        ten += 1
    
if five == 0 and one == 0 and ten == 0:
    print(-1)
else:
    print(five, one, ten)