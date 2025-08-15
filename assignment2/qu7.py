SP=int(input("Enter the selling price:"))
CP=int(input("Enter the cost price:"))
if (SP>CP):
    print("This transaction incurred profit of ", SP-CP)
elif (CP>SP):
    print("This transaction incurred loss of ", CP-SP)