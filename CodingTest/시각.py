n = int(input())

#N시 59분 59초까지 3이 포함..
result = 0

for hour in range(n + 1):
    for minutes in range(60):
        for second in range(60):
            if '3' in str(hour) + str(minutes) + str(second):
                result += 1
print(result)