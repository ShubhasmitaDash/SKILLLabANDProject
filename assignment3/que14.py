#wap to print the "nth" digit of a number from the right
num_str=input("enter the number:")
n_str=input("enter the nth digit from the right:")

try:
    n = int(n_str)
    if not num_str.isdigit():
        print("Error: The number must contain only digits.")
    elif n <= 0:
        print("Error: The position 'n' must be a positive number.")
    elif n > len(num_str):
        print(f"Error: The number '{num_str}' only has {len(num_str)} digits. Cannot find the {n}th digit.")
    else:
        digit = num_str[-n]
        print(f"The {n}th digit of {num_str} from the right is: {digit}")

except ValueError:
    print("Invalid input for the position. Please enter a whole number.")