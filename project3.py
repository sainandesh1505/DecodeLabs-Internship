import random
import string

def generate_password():
    # Ask the user for the desired password length
    try:
        length = int(input("Enter the desired password length: "))
        
        if length < 4:
            print("Password length should be at least 4 for better security.")
            return

        # Define the pool of characters to choose from
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate the password using random.choices
        password = ''.join(random.choices(characters, k=length))
        
        print(f"\nGenerated Password: {password}")
        
    except ValueError:
        print("Invalid input! Please enter a numeric value for the length.")

# Run the generator
if __name__ == "__main__":
    generate_password()
