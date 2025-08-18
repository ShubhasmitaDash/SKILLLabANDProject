n=int(input("Enter the nth term:"))
sum=0
for i in range(1,n+1):
    for j in range(1, n+1, 2):
        sum=(i/j)+sum
print("Sum of the series is",sum)