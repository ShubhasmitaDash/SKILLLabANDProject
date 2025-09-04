try:
    with open("notes.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("File operation complete.\n")