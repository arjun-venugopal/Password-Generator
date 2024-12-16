import secrets
import string
import re

class PasswordGenerator:
    def __init__(self, length: int = 12, uppercase: bool = True,
                 lowercase: bool = True, numbers: bool = True,
                 symbols: bool = True) -> None:
        
        """
        Initializes the password generator with customizable settings.

        Args:
            length (int): Length of the password to be generated.
            uppercase (bool): Include uppercase letters.
            lowercase (bool): Include lowercase letters.
            numbers (bool): Include numbers.
            symbols (bool): Include special symbols.
        """
        
        self.length = length
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.numbers = numbers
        self.symbols = symbols

    def generate(self) -> str:
        # Build character pool based on flags
        characters = ''
        if self.uppercase:
            characters += string.ascii_uppercase
        if self.lowercase:
            characters += string.ascii_lowercase
        if self.numbers:
            characters += string.digits
        if self.symbols:
            characters += string.punctuation

        if not characters:
            raise ValueError("At least one character type must be selected.")

        # Generate the password
        return ''.join(secrets.choice(characters) for _ in range(self.length))
    
    @staticmethod
    def check_password_strength(password: str)->str:
        """
          Check the strength of a password based on multiple criteria.
        
        Args:
            password (str): The password to evaluate.
        
        Returns:
            str: Password strength as 'Weak', 'Moderate', or 'Strong'.
        """

        score = 0  # Initialize the score to 0

        # Rule 1: Minimum length requirement
        if len(password) >= 8:
            score += 1
        if len(password) >= 12:
            score += 1  # Extra point for longer passwords

        # Rule 2: Presence of character diversity
        if any(char.isupper() for char in password):
            score +=1
        if any(char.islower() for char in password):
            score += 1
        if any(char.isdigit() for char in password):
            score +=1
        if any(char in string.punctuation for char in password):
            score += 1

        #Rule 3: avoid common passwords
        weak_patterns = [
            r'1234|2345|abcd|qwerty|asdf',  # Sequential characters or keyboard patterns
            r'(.)\1{2,}',                   # Repeated characters
            r'password|welcome|admin',      # Common weak words
            r'19[0-9]{2}|20[0-2][0-9]',     # Dates/years
            r'(abc|123)\1',                 # Repeated patterns
            r'p@ssw0rd|adm1n'               # Leetspeak
        ]
        
        if not (re.search(pattern, password, re.IGNORECASE) for pattern in weak_patterns):
                score += 1

        # Determine the password strength based on the score
        if score <=3:
            return 'Weak'
        elif 4 <= score <= 7:
            return 'Moderate'
        else:
            return 'Strong'

        
    def main(self):
        """
        Main execution method for password generation and strength checking.
        """
        print("1. Generate a password")
        print("2. Evaluate a password")
        choice = input("Select an option (1 or 2): ").strip()

        if choice == '1':
            password = self.generate()
            print(f"Generated Password: {password}")
        elif choice == '2':
            password = input('Enter your password to evaluate: ').strip()
        else:
            print("Invalid choice. Exiting.")
            return

        password_strength = self.check_password_strength(password)
        print(f"Password Strength: {password_strength}")
        
if __name__ == '__main__':
    PasswordGenerator().main()
