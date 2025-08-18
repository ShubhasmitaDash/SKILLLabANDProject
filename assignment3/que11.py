#wap to find the numbers, which are divisible by the sum of their digits between 1 to 1000
for i in range(1,10001):
    sum=0
    num=i
    while(num!=0):
        rem=num%10
        sum=sum+rem
        num=num//10
    if i%sum==0:
        print(i)
    else:
        continue