age=int(input("Enter the age:"))
if (age in range(0, 12)):
    print("Child")
elif (age in range(13, 19)):
    print("Teenager")
elif (age in range(20,59)):
    print("Adult")
elif (age in range(60,100)):
    print("Senior Citizen")