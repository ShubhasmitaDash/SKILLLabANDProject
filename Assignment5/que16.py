s=input("Enter a String:")
for i in s:
    if i in ["a","e","i","o","u","A","E","I","O","U"]:
        s=s.replace(i,"*")
print(s)