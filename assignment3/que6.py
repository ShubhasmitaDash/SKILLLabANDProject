num=int(input("enter the number: "))
rev=0
num1=num
while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
if num1==rev:
    print("palindrome")
else:
    print("not palindrome")