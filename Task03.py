import re

def check_password_strength(password):
    strength_points = 0
    criteria = {
        "length": len(password) >= 8,
        "uppercase": re.search(r"[A-Z]", password) is not None,
        "lowercase": re.search(r"[a-z]", password) is not None,
        "digit": re.search(r"[0-9]", password) is not None,
        "special_char": re.search(r"[@$!%*?&]", password) is not None
    }

    # Calculate strength points
    for key, passed in criteria.items():
        if passed:
            strength_points += 1

    # Assess strength
    if strength_points == 5:
        strength = "Very Strong 💪"
    elif strength_points == 4:
        strength = "Strong 👍"
    elif strength_points == 3:
        strength = "Moderate 😐"
    elif strength_points == 2:
        strength = "Weak ⚠️"
    else:
        strength = "Very Weak ❌"

    return strength, criteria

# Example usage
if __name__ == "__main__":
    pwd = input("Enter a password: ")
    strength, details = check_password_strength(pwd)

    print("\n--- Password Analysis ---")
    print("Password:", pwd)
    print("Strength:", strength)
    print("Criteria:")
    for c, status in details.items():
        print(f"  {c}: {'✔️' if status else '❌'}")