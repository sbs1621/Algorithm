n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()

count = 0
for i in range(n):
    count += A[i] * B[i]

print(count)
