try:
    filename = "user_input.txt"
    with open(filename, "w") as file:
        text = input("Enter text to write into file: ")
        file.write(text)
    print(f"Data written to {filename} successfully.")
except OSError:
    print("Error: Could not open or write to file.")