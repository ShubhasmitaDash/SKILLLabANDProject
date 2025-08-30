password=input("Enter your password:")
mobile=input("Enter your mobile number:")
if password.isalnum:
    print("Password is correct")
else:
    print("password should be alphanumeric only")
if len(mobile)!=10:
    print("Enter correct phone number:")
else:
    print("Phone number is correct")