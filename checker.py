import re

def check_password(password):
    issues = []

    if len(password) < 8:
        issues.append("Password is too short (minimum 8 characters).")

    if not re.search(r"[A-Z]", password):
        issues.append("Missing uppercase letter.")

    if not re.search(r"[a-z]", password):
        issues.append("Missing lowercase letter.")

    if not re.search(r"[0-9]", password):
        issues.append("Missing number.")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        issues.append("Missing special character.")

    return issues

password = input("Enter a password to analyze: ")
problems = check_password(password)

if problems:
    print("\nPassword is WEAK:")
    for issue in problems:
        print(f"- {issue}")
else:
    print("\nPassword is STRONG")
