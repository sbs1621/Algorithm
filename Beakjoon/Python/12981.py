R, G, B = map(int, input().split())


count = R // 3 + G // 3 + B // 3
while True:
    if R % 3 == 0 and G % 3 == 0 and B % 3 == 0:
        break

    
    if R % 3 > 0 and G % 3 > 0 and B % 3 > 0:
        R -= 1
        G -= 1
        B -= 1
        count += 1


    if R % 3 == 0:
        if G % 3 == 0 and B % 3 != 0:
            count += 1
            break
        if B % 3 == 0 and G % 3 != 0:
            count += 1
            break
        if G % 3 != 0 and B % 3 != 0:
            if G % 3 == 1 and B % 3 == 1:    
                count += 1
            else:
                count += 2
            break

    elif G % 3 == 0:
        if R % 3 == 0 and B % 3 != 0:
            count += 1
            break
        if B % 3 == 0 and R % 3 != 0:
            count += 1
            break
        if R % 3 != 0 and B % 3 != 0:
            if R % 3 == 1 and B % 3 == 1:    
                count += 1
            else:
                count += 2
            break
        print(count)

    elif B % 3 == 0:
        if R % 3 == 0 and G % 3 != 0:
            count += 1
            break
        if G % 3 == 0 and R % 3 != 0:
            count += 1
            break
        if R % 3 != 0 and G % 3 != 0:
            if R % 3 == 1 and G % 3 == 1:    
                count += 1
            else:
                count += 2
            break



   
 

print(count) 