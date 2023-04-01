import string

def test_password():
    password = input("Enter password: ")

    """
    uppercase = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lowercase = any([1 if c in string.ascii_lowercase else 0 for c in password])
    special_char = any([1 if c in string.punctuation else 0 for c in password])
    digits = any([1 if c in string.digits else 0 for c in password])
    """
    character = set()
    for c in password:
        if c in string.ascii_uppercase:
            uppercase = True
            character.add(uppercase)
        if c in string.ascii_lowercase:
            lowercase = True
            character.add(lowercase)
        if c in string.punctuation:
            special_char = True
            character.add(special_char)
        if c in string.digits:
            digits = True
            character.add(digits)

    score = 0


    if len(password) > 4:
        score += 1
    if len(password) > 6:
        score += 1
    if len(password) > 8:
        score += 1
    if len(password) > 12:
        score += 1

    if uppercase:
        score += 1
    if lowercase:
        score += 1
    if special_char:
        score += 1
    if digits:
        score += 1
    
    return score


def main():
    score = test_password()
    print(score)
    if 8 <= score > 6:
        print("The password is Strong")
    elif score > 6:
        print("The password is alright")
    elif score > 4:
        print("The password is weak")
    else:
        print("invalid password...try again")

main()
