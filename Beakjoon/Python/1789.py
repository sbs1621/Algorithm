n = int(input())

count = 0
cnt = 0
if n == 1:
    print(1)
    exit()
    
for i in range(0,n):
    count += i + 1
    if count > n:
        print(cnt)
        break
    cnt += 1