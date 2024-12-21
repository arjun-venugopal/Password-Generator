from use_cases.password_generator import PasswordGenerator
from entities.password import Password

class CLI:
    def __init__(self, generator: PasswordGenerator) -> None:
        self.generator = generator

    def prompt(self):
        print("1. Generate a password")
        print("2. Evaluate a password")
        choice = input("Select an option (1 or 2): ").strip()

        if choice == '1':
            password = self.generator.generate()
            print(f"Generated Password: {password}")
            print(f"Password Strength: {self.generator.check_password_strength(password)}")
        elif choice == '2':
            password = input('Enter your password to evaluate: ').strip()
            password_strength = self.generator.check_password_strength(password)
            print(f"Password Strength: {password_strength}")
        else:
            print("Invalid choice. Exiting.")
