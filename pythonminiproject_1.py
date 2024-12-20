def check_password_strength(password):
    
    strength_score = 0
    suggestions = []

    
    if len(password) < 8:
        suggestions.append("Password should be at least 8 characters long.")
    else:
        strength_score += 1

    
    if any(c.isupper() for c in password):
        strength_score += 1
    else:
        suggestions.append("Password should contain at least one uppercase letter.")

    
    if any(c.islower() for c in password):
        strength_score += 1
    else:
        suggestions.append("Password should contain at least one lowercase letter.")

    
    if any(c.isdigit() for c in password):
        strength_score += 1
    else:
        suggestions.append("Password should contain at least one digit.")

    
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

    
    print(f"Password Strength Score: {strength_score}")
    if strength_score == 5:
        print("Your password is strong!")
    else:
        print("Suggestions for a stronger password:")
        for suggestion in suggestions:
            print(f"- {suggestion}")



password = input("Enter a password to analyze: ")
check_password_strength(password)
