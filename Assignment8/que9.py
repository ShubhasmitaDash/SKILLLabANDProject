numbers = [10, 20, 30, 40, 50]
with open("numbers2.txt", "w") as file:
    for num in numbers:
        file.write(str(num) + "\n")