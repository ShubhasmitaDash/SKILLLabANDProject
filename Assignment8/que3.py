with open("notes.txt", "r") as file:
    content = file.read()
    words = content.split()
    lines = content.splitlines()
print("Characters:", len(content))
print("Words:", len(words))
print("Lines:", len(lines), "\n")