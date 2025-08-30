password = input("enter the password")
has_lowercase = False
has_uppercase = False
has_digit = False
for char in password:
    if char.islower():
        has_lowercase = True
    elif char.isupper():
        has_uppercase = True
    elif char.isdigit():
        has_digit = True
if has_lowercase and has_uppercase and has_digit:
    print("valid password")
else:
    print("invalid password")