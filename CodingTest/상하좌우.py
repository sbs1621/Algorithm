n = int(input())
str = input()
move = str.split(' ')
x = 1
y = 1
for i in range(len(move)):
    if move[i] == "U":
        if x != 1:
            x -= 1
    if move[i] == "D":
        if x != n:
            x += 1
        
    if move[i] == "L":
        if y != 1:
            y -= 1
        
    if move[i] == "R":
        if y != n:
            y += 1
    
print(x,y)    