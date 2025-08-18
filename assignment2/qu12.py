a=int(input("Enter the marks of first subject:"))
b=int(input("Enter the marks of second subject:"))
c=int(input("Enter the marks of third subject:"))
avg=(a+b+c)/3
if (avg>=90):
    print("Grade A")
elif (avg>=80):
    print("Grade B")
elif(avg>=70):
    print("Grade C")
elif(avg>=60):
    print("Grade D")
else:
    print("Grade F")