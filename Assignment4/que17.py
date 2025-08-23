b="Python is fun"
list=b.split(sep=" ")
print(list)
a=""
for i in list:
    a=a+i
    if i!=list[-1]:
        a=a+"-"
print(a)
print(type(a))
