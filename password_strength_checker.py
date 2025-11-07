password = input("Enter a password: ")

length = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_symbol = any(c in "!@#$%^&*()-_=+[]{};:,.<>?/" for c in password)

score = 0
if length >= 8:
    score += 1
if has_upper and has_lower:
    score += 1
if has_digit:
    score += 1
if has_symbol:
    score += 1
if length >= 12:
    score += 1  # bonus for long passwords

if score <= 2:
    strength = "Weak"
elif score == 3 or score == 4:
    strength = "Medium"
else:
    strength = "Strong"

print("\nPassword Strength:", strength)
print("Length:", length)

# Suggestions
suggestions = []
if length < 8:
    suggestions.append("Use at least 8 characters.")
if not has_upper:
    suggestions.append("Add uppercase letters (A-Z).")
if not has_lower:
    suggestions.append("Add lowercase letters (a-z).")
if not has_digit:
    suggestions.append("Add numbers (0-9).")
if not has_symbol:
    suggestions.append("Add symbols (e.g., !@#$%).")

if suggestions:
    print("\nSuggestions:")
    for s in suggestions:
        print("-", s)
else:
    print("\nGood job! Your password looks strong.")
