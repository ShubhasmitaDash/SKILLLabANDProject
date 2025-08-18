#wap to find the nearest number to 1000, which is less than 1000, and divisible by 18 and 32
for i in range(1000,0,-1):
    if i%18==0 and i%32==0:
        print(i)
        break
    else:
        continue