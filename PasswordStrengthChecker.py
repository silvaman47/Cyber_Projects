import re

def check_password_strength(password):
    # Initialize scores
    length_score = 0
    upper_lower_score = 0
    number_score = 0
    special_char_score = 0

    # Check password length
    if len(password) >= 8:
        length_score = 1

    # Check for both uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        upper_lower_score = 1

    # Check for numbers
    if re.search(r'\d', password):
        number_score = 1

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        special_char_score = 1

    # Total score
    total_score = length_score + upper_lower_score + number_score + special_char_score

    # Give feedback based on total score
    if total_score <= 1:
        return "Weak"
    elif total_score == 2 or total_score == 3:
        return "Moderate"
    else:
        return "Strong"

# Let’s test it
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Your password is: {strength}")
