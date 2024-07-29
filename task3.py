import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check for numbers
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Determine password strength
    if strength == 5:
        feedback.append("Your password is very strong.")
    elif 3 <= strength < 5:
        feedback.append("Your password is strong.")
    elif 1 <= strength < 3:
        feedback.append("Your password is weak.")
    else:
        feedback.append("Your password is very weak.")

    return feedback

def main():
    while True:
        password = input("Enter a password to assess (or type 'q' to quit): ")
        if password.lower() == 'q':
            break

        feedback = assess_password_strength(password)
        print("\nPassword Strength Assessment:")
        for comment in feedback:
            print(f"- {comment}")
        print()

if __name__ == "__main__":
    main()
