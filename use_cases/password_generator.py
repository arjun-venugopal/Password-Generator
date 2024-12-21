import secrets
import string
from entities.password import Password

class PasswordGenerator:
    def __init__(self, password: Password) -> None:
        self.password = password

    def generate(self) -> str:
        """
        Generates a random password based on character pool.
        """
        characters = self.password.get_character_pool()
        password = ''.join(secrets.choice(characters) for _ in range(self.password.length))

        # Ensure the password includes at least one of each selected character type
        while (self.password.uppercase and not any(char.isupper() for char in password)) or \
              (self.password.lowercase and not any(char.islower() for char in password)) or \
              (self.password.symbols and not any(char in string.punctuation for char in password)):
              (self.password.symbols and not any(char in string.punctuation for char in password))
        password = ''.join(secrets.choice(characters) for _ in range(self.password.length))

        return password

    def check_password_strength(self, password: str) -> str:
        """
        Checks the strength of the given password.
        """
        return self.password.check_strength(password)
