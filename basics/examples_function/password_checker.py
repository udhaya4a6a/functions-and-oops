def is_strong_password(password):
    """
    Check if the given password is strong.
    A strong password is defined as one that is at least 8 characters long,
    contains both uppercase and lowercase letters, at least one digit,
    and at least one special character.

    Args:
        password (str): The password to check.
        """
    if len(password) <8:
        print("Password must be at least 8 characters long.")
        return False
        
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        return False
    
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        return False
        
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        return False

    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password):
        print("Password must contain at least one special character.")
        return False
        
    print("Password is strong.")
    return True
# Example usage

while True:
    password = input("Enter your password to check if it's strong: ")

    if is_strong_password(password):
        break
    else:
        print("Please try again.\n")
