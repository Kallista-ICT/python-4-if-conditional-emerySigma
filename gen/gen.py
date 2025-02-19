yearInput = int(input("Please enter year of birth: "))

if yearInput < 1946:
    category = "Silent Generation"
elif yearInput < 1965:
    category = "Baby Boomer"
elif yearInput < 1981:
    category = "Generation X"
elif yearInput < 1997:
    category = "Millennials"
elif yearInput < 2013:
    category = "Generation Z"
elif yearInput < 2026:
    category = "Generation Alpha"

print(f"You Belong to: {category}")