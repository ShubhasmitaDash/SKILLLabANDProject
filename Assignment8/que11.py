try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result =", result)
except ValueError:
    print("Error: Please enter numeric values.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.\n")