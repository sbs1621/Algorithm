n = int(input())

owner = list(map(int, input().split()))
me = list(map(int, input().split()))
owner.sort(reverse=True)
me.sort()

count = 0
for i in range(n):
    if owner[n -i- 1] < me[0]: #min(owner) < min(me)
        count += 1
        del(owner[n -i- 1], me[0])
    elif owner[0] > me[0]:
        count -= 1
        del(owner[0], me[0])

if count > 0:
    print("YES")
else:
    print("NO")