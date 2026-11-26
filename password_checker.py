import getpass

common_passwords = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "password123",
    "welcome",
    "iloveyou",
    "111111",
    "pass123",
    "pass@123",
    "admin@123",
    "123123",
    "112233",
    "12345678910"
]


def check_password(password):
    score = 0
    suggestions = []

    # 1. Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # 2. Check special characters
    if any(not char.isalnum() and not char.isspace() for char in password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    # 3. Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    # 4. Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    # 5. Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Determine password strength
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return score, strength, suggestions


def main():
    password = getpass.getpass("Enter your password: ")

    if not password:
        print("Password cannot be empty!")
        return

    # Check common password
    if password.lower() in common_passwords:
        print("Warning: This is a common password!")
   

    score, strength, suggestions = check_password(password)

    print("\nPassword Score:", score, "/5")
    print("Password Strength:", strength)

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("\nGreat! Your password meets all basic requirements.")


main()   