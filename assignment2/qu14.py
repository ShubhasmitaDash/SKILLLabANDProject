unit=int(input("Enter the number of units:"))
if unit>=100:
    total=5*unit
elif unit in range(101, 200):
    total=100*5+(unit-100)*7
else:
    total=100*5+100*7+(unit-200)*10
print("The total price of the units consumed is:", total)