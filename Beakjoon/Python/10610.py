number = input()
numList = list(map(int, str(number)))
numList.sort()
thirty = 0
count = 1
result = 0
if "0" not in number:
    print(-1)
else:
    for i in range(len(numList)):
        thirty += numList[i]
    if thirty % 3 == 0:
        for i in range(len(numList)):
            if i == 0:
                result += numList[i] 
            else:
                count *= 10
                result += numList[i]* count
                
        print(result)
    else:
        print(-1)
