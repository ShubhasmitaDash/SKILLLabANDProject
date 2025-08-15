a=int(input("Enter the coefficient of x1 in first equation:"))
b=int(input("Enter the coefficient of x2 in first equation:"))
m=int(input("Enter the constant in first equation:"))
c=int(input("Enter the coefficient of x1 in second equation:"))
d=int(input("Enter the coefficient of x2 in second equation:"))
n=int(input("Enter the constant in second equation:"))
if (a*d-c*b)==0:
    print("The denominator becomes equal to zero")
else:
    x1=(m*d-n*b)/(a*d-c*b)
    x2=(n*a-m*c)/(a*d-c*b)
    print("value of x1", x1)
    print("value of x2", x2)

