A,B,C,D,E = map(int, input().split())

count = E + D
A -= D

while C > 0:
    count += 1
    if B > 0:
        B -= 1
        C -= 1
    elif A > 0:
        A -= 2
        C -= 1
    else:
        C -= 1


while B > 0:
    count += 1
    if B > 1 and A > 0:
        B -= 2
        A -= 1
    elif B > 0 and A > 0:
        B -= 1
        A -= 3
    else:
        B -= 2

while A > 0:
    count += 1
    A -= 5

print(count)