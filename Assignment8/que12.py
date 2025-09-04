try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Enter an integer.")
else:
    print("Square:", num ** 2, "\n")