import string
import re

class Password:
    def __init__(self, length: int = 16, uppercase: bool = True,
                 lowercase: bool = True, numbers: bool = True,
                 symbols: bool = True) -> None:
        self.length = length
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.numbers = numbers
        self.symbols = symbols

    def get_character_pool(self) -> str:
        """
        Returns a string of available characters based on settings.
        """
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
            raise ValueError("No character types selected for password generation.")
        return characters

    def check_strength(self, password: str) -> str:
        """
        Determines the strength of a password based on various rules.
        """
        score = 0
        # Length check
        if len(password) < 8:
            return 'Weak'
        elif len(password) >= 12:
            score += 2
        else:
            score += 1

        # Character diversity check
        if any(char.isupper() for char in password):
            score += 1
        if any(char.islower() for char in password):
            score += 1
        if any(char.isdigit() for char in password):
            score += 1
        if any(char in string.punctuation for char in password):
            score += 1

        # Check for weak patterns
        weak_patterns = [
            r'1234|2345|abcd|qwerty|asdf',
            r'(.)\1{2,}',
            r'password|welcome|admin',
            r'19[0-9]{2}|20[0-2][0-9]',
            r'(abc|123)\1',
            r'p@ssw0rd|adm1n'
        ]
        if any(re.search(pattern, password, re.IGNORECASE) for pattern in weak_patterns):
            score -= 2

        # Strong password criteria
        has_all_types = all([
            any(char.isupper() for char in password),
            any(char.islower() for char in password),
            any(char.isdigit() for char in password),
            any(char in string.punctuation for char in password)
        ])
        
        if score >= 4 and has_all_types:
            return 'Strong'
        elif score >= 2:
            return 'Moderate'
        return 'Weak'
