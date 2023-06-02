A,B,C,D,E,F = map(int, input().split())

if B == D:
    H = F
elif B == F:
    H = D
else:
    H = B

if A == C:
    G = E
elif A == F:
    G = C
else:
    G = A

print(G, H)