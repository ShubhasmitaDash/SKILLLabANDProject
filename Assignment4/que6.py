n=int(input("Enter the last number:"))
list=[]
for i in range(1,n+1):
    list.append(i)
print("Sum of the numbers:")
print(sum(list))
print("Average of the numbers:")
print(sum(list)/len(list))
print("Maximum of the numbers:")
print(max(list))
print("Minimum of the numbers:")
print(min(list))