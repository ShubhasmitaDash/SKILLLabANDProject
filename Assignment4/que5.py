n=int(input("Enter the last number to be in list:"))
list=[]
for i in range(n+1):
    list.append(i)
num=int(input("Enter the number to be searched:"))
if num in list:
    print("Found")
else:
    print("Not found")