import random
import string

def get_user_choice(prompt):
    return input(prompt).strip().lower() == 'y'

def generate_password():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be greater than 0.")
            return

        print("Choose character types to include:")
        chars = ''
        if get_user_choice("Include uppercase? (y/n): "):
            chars += string.ascii_uppercase
        if get_user_choice("Include lowercase? (y/n): "):
            chars += string.ascii_lowercase
        if get_user_choice("Include digits? (y/n): "):
            chars += string.digits
        if get_user_choice("Include symbols? (y/n): "):
            chars += string.punctuation

        if not chars:
            print("Error: At least one character type must be selected.")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"\nGenerated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter a number.")

generate_password()
