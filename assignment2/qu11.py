op=input("+ or - or * or /")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    print(a/b)
else:
    print("Invalid operator")