with open("notes.txt", "r") as file:
    words = file.read().split()
print("Total words =", len(words), "\n")