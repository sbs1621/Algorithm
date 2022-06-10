
from sys import addaudithook


arraySize, addArray, repeat = map(int, input().split())

arrayData = list(map(int, input().split()))

arrayData.sort();

firstNumber = arrayData[arraySize-1]
secondNumber = arrayData[arraySize-2]
print(arrayData)

result =0
count = 1
for i in range(repeat):
 
    if count != addArray:
        result += firstNumber
        print(i,',' ,result)
        count += 1
    else:
        result += secondNumber
        print(i,',' ,result)
        count = 0
    

print(result)
