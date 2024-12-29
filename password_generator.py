import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special_chars=True):
    # Define character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if include_uppercase else ''
    number_chars = string.digits if include_numbers else ''
    special_chars = string.punctuation if include_special_chars else ''
    
    # Combine all character sets
    all_chars = lowercase_chars + uppercase_chars + number_chars + special_chars
    
    # Ensure the password includes at least one character from each selected set
    password = [
        random.choice(lowercase_chars),
        random.choice(uppercase_chars) if include_uppercase else '',
        random.choice(number_chars) if include_numbers else '',
        random.choice(special_chars) if include_special_chars else ''
    ]
    
    # Fill the rest of the password length with random choices from the combined set
    password += random.choices(all_chars, k=length - len(password))
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    # Join the list into a string and return
    return ''.join(password)

# Example usage
print(generate_password(length=16))