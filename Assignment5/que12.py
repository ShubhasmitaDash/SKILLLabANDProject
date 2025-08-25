str1=input("Enter a string:")
l1=[]
l2=[]
for i in str1:
    if i not in l1:
        l1.append(i)
    l2.append(str1.count(i))
print(l1)  
print(l2)
