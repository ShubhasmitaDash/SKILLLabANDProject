#program to check whether thedigits of a given number are equal
num=int(input("enter the number:"))
num1=num
count=0
while(num!=0):
    rem=num%10
    num=num//10
    count=count+1
num=num1
sum=0
while(num!=0):
    rem=num%10
    sum=sum+rem
    num=num//10
if sum%count==0:
    print("equal")
else:
    print("not equal")