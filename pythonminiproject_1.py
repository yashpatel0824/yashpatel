def check_password_strength(password):
    # Initialize the strength score and suggestions list
    strength_score = 0
    suggestions = []

    # Check password length
    if len(password) < 8:
        suggestions.append("Password should be at least 8 characters long.")
    else:
        strength_score += 1

    # Check for uppercase letter
    if any(c.isupper() for c in password):
        strength_score += 1
    else:
        suggestions.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letter
    if any(c.islower() for c in password):
        strength_score += 1
    else:
        suggestions.append("Password should contain at least one lowercase letter.")

    # Check for digit
    if any(c.isdigit() for c in password):
        strength_score += 1
    else:
        suggestions.append("Password should contain at least one digit.")

    # Check for special character
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"
    contains_special = False
    for char in password:
        if char in special_chars:
            contains_special = True
            break

    if contains_special:
        strength_score += 1
    else:
        suggestions.append("Password should contain at least one special character.")

    # Output result
    print(f"Password Strength Score: {strength_score}")
    if strength_score == 5:
        print("Your password is strong!")
    else:
        print("Suggestions for a stronger password:")
        for suggestion in suggestions:
            print(f"- {suggestion}")


# Example password check
password = input("Enter a password to analyze: ")
check_password_strength(password)
