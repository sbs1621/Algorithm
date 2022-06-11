W, M, I = map(int, input().split())
count = 0
for i in range(I):
    if W == M*2:
        W -= 1
    elif W > M*2:
        W -= 1
    elif W < M*2:
        M -= 1

while True:
    W -= 2
    M -= 1
    if W < 0 or M < 0:
        break
    count += 1

print(count)    