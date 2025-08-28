#Write a Python program that counts the frequency of each word in the string:
#”Python is fun and Python is powerful”. Store the result in a dictionary.
str="Python is fun and Python is powerful"
l=str.split()
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)