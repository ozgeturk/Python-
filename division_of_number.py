x = int(input())

count = 1
print(x, end=" ")
while x != 1 and x != 0:
    if x % 2 == 0:
        if count < 20:
            x = x // 2
            count += 1
            print(x, end=" ")
        else:
            break

    elif x % 2 == 1:
        if count < 20:
            x = (x * 3) + 1
            count += 1
            print(x, end=" ")
        else:
            break
            
