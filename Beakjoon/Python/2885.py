n = int(input());

check = 1
for i in range(n):
    if check >= n:
        break
    check *= 2
print(check, end = " ")
count = 0
for i in range(n):
    if n % check == 0:
        print(count)
        break
    else:
        check = check / 2
        count += 1