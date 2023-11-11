import re

def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        return True
    else:
        return False

email = input("Please enter your email address: ")

if validate_email(email):
    print(f"The email '{email}' is valid.")
else:
    print(f"The email '{email}' is invalid.")