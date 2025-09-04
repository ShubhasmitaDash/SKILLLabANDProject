#Create a text file with multiple lines. Write a program to read the file and print its
#content line by line.
f1=open("notes.txt","r")
print(f1.read())
f1.close()