list=[5, 10, 15, 20, 25, 50, 20]
for i in list:
    if i==20:
        list.insert(list.index(i)+1,200)
        list.remove(20)
print(list)