import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    # Create a pool of characters to choose from based on user preferences
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    # Ensure there are characters to choose from
    if not characters:
        raise ValueError("At least one character type must be selected")

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Prompt the user for password criteria
    length = int(input("Enter the desired password length: "))
    
    print("Include the following character types in the password:")
    use_letters = input("Letters (y/n): ").lower() == 'y'
    use_numbers = input("Numbers (y/n): ").lower() == 'y'
    use_symbols = input("Symbols (y/n): ").lower() == 'y'
    
    try:
        # Generate the password
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        
        # Display the generated password
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
