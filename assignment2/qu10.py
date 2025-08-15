a=int(input("Enter one side of triangle:"))
b=int(input("Enter second side of triangle :"))
c=int(input("Enter third side of triangle :"))
if a==b==c:
    print("This is an equilateral triangle")
elif(a==b or b==c or c==a):
    print("This is an isosceles triangle")
