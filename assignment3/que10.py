#wap to write fibonacci series
n=int(input("enter the number of terms:"))
a=0
b=1
if n <= 0:
    print("Please enter a positive number of terms.")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
