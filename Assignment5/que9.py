furniture=[]
price=[]
while(1):
    a=input("Enter the furniture:")
    furniture.append(a)
    b=int(input("Enter the price:"))
    d=int(input("Enter the quantity of the furniture:"))
    price.append(b*d)
    c=input("Do you want to enter more furniture? Yes or No")
    if c=="No":
        break
t1=tuple(furniture)
t2=tuple(price)
s=sum(t2)
print(t1)
print("price",t2)


