#Wap for armstrong number
num=int(input("enter the number:"))
sum=0
num1=num
while(num!=0):
    rem=num%10
    sum=sum+pow(rem,3)
    num=num//10
if num1==sum:
    print("armstrong number")
else:
    print("not armstrong number")