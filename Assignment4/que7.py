list=[1, 1, 2, 3, 4, 4, 4, 5, 3, 6, 7, 4]
list2=[]
for i in list:
    list2.append(i)
    if i in list:
        print("",i,":",list.count(i))
    else:
        break

