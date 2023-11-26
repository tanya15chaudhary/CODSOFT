import random
import string

def generate_password(length=12):
    # Define characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by sampling from the characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Example: Generate a password with default length (12 characters)
password = generate_password()
print("Generated Password:", password)
