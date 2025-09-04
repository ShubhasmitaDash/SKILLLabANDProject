search_word = "Line"
print("Searching for word:", search_word)
with open("notes.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        if search_word in line:
            print(f"Word found in line {i}")
print()