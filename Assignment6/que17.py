set1={10,20,30,40,50}
set2={30,40,50,60,70}
s1= set1 & set2
for i in s1:
    if i not in set2 or i not in set1:
        set1.remove(i)
        set2.remove(i)
print(set1)
print(set2)

        