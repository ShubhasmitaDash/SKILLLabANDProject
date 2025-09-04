word_to_search = "Python"
print("Searching for word:", word_to_search)
with open("notes.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        if word_to_search in line:
            print(f"Found in line {i}: {line.strip()}")
print()