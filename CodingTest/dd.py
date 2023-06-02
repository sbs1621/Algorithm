def recursive(n):
    if n == 1:
        return 1
    else:
        return 4 * recursive(n-1) + 3

# 테스트
n = int(input())
result = recursive(n)
print(result)