print("Q14 Output:")
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    print("Valid age:", age)
except ValueError as e:
    print("Error:", e, "\n")