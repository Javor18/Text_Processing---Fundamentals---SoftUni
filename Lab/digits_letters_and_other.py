text = input()

digits = ""
letters = ""
other = ""

for character in text:
    if character.isdigit():
        digits += character

    elif character.isalpha():
        letters += character

    else:
        other += character

print(digits)
print(letters)
print(other)