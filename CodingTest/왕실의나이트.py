n = input()

row = int(n[1])
column = int(ord(n[0])) - int(ord('a')) + 1
step = [(-2,-1), (-1,-2), (2, -1,), (-1,2), (-2,1), (1, -2), (2,1), (1,2)]

result = 0
for i in step:
    if row + i[0] >=1 and row + i[0] <=8 and column + i[1] >=1 and column + i[1] <= 8:
        result += 1
        
print(result)