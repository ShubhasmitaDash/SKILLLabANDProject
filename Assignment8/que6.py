with open("notes.txt", "r") as file:
    line_count = sum(1 for _ in file)
print("Number of lines =", line_count, "\n")