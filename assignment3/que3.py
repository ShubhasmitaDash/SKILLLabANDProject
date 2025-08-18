import math
n=int(input("Enter the n natural numbers:"))
sum=0
for i in range(1,n+1):
    sum=math.pow(i,2)+sum
print("Sum of the n square numbers is",sum)