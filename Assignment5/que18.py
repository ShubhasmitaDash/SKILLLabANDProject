email=input("Enter your email:")
if "@" in email:
    print("Valid email with @ at", email.index("@"))
else:
    print("Invalid email")