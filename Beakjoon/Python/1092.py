n = int(input())
w = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

w.sort(reverse=True)
b.sort(reverse=True)

count = 0

if w[0] < b[0]:
    print("-1")
    exit()

while len(b) != 0:
    count += 1
    i = 0
    j = 0
    while i < n and len(b) != 0:
        while j < len(b):
            if w[i] >= b[j]:
                del b[j]
                break
            else:
                j += 1
        i += 1

print(count)