n = int(input())

dataM = []
dataP = []
data0 = []
for _ in range(n):
    m = int(input())
    if m == 0:
        data0.append(m)
    elif m > 0:
        dataP.append(m)
    else:
        dataM.append(m)

dataP.sort(reverse=True)
dataM.sort()



count = 0
while True:
    if len(dataP) > 1:
        if dataP[0] + dataP[1] > dataP[0] * dataP[1]:
            count += dataP[0] + dataP[1]
        else:
            count += dataP[0] * dataP[1]
        del dataP[1], dataP[0]
    if len(dataP) == 1:
        count += dataP[0]
        del dataP[0]
    
    if len(dataM) > 1:
        count += dataM[0] * dataM[1]
        del dataM[1], dataM[0]

    if len(dataM) == 1 and len(data0) == 0:
        count += dataM[0]
        del dataM[0]

    if len(dataP) == 0 and len(dataM) <=1:
        break
        
print(count)    