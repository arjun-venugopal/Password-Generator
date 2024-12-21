from entities.password import Password
from use_cases.password_generator import PasswordGenerator
from interface_adapters.cli import CLI

def main():
    password = Password(length=16, uppercase=True, lowercase=True, numbers=True, symbols=True)
    password_generator = PasswordGenerator(password)
    cli = CLI(password_generator)
    cli.prompt()

if __name__ == '__main__':
    main()
