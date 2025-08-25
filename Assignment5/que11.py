string1=input("Enter one string:")
string2=input("Enter another string:")
result=string1+string2
l1=result.split()
l2=str(l1)
l3=[]
for i in l2:
    if i.isupper():
        l3.append(i)
print(l3)
