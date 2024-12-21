Here is the **README.md** file tailored for the password generator and strength checker code you provided:

---

# Password Generator & Strength Checker

A secure password generator that allows customizable password generation and strength evaluation. The application lets users configure password length, character sets (uppercase, lowercase, digits, symbols), and checks the strength of the generated or entered passwords.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)

## Description

This is a Python-based application that provides two key functionalities:
1. **Password Generation**: Generate secure random passwords based on user-selected options.
2. **Password Strength Checking**: Evaluate the strength of a password, classifying it as weak, moderate, or strong.

The password generator ensures cryptographically secure randomness using the `secrets` module and checks password strength based on several criteria such as length, diversity of character types, and known weak patterns.

## Features

- **Customizable Password Generation**: Choose length, inclusion of uppercase letters, lowercase letters, digits, and special characters.
- **Password Strength Evaluation**: Checks passwords against rules and rates them as "Weak", "Moderate", or "Strong".
- **Secure Password Generation**: Uses Python’s `secrets` module to generate cryptographically secure passwords.
- **User-Friendly CLI**: Interact with the application using a simple command-line interface.

## Installation

Follow the steps below to install and run the password generator and strength checker.

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/arjun-venugopal/Password-Generator.git
   cd password-generator
   ```

2. **Create a Virtual Environment** (Optional, but recommended):

   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```


## Usage

Once installed, you can run the application by executing the following command:

```bash
python run.py
```

### Command-Line Interface

The user will be presented with a menu to either:
1. Generate a new secure password.
2. Evaluate the strength of an existing password.

Example output:
```bash
1. Generate a password
2. Evaluate a password
Select an option (1 or 2): 1
```

If "1" is selected, the application generates and displays a secure password. If "2" is selected, the user is prompted to input an existing password to evaluate its strength.

### Example of Password Generation

```bash
1. Generate a password
2. Evaluate a password
Select an option (1 or 2): 1
Generated Password: Gt7@Vm4b#
Password Strength: Strong
```

### Example of Password Evaluation

```bash
1. Generate a password
2. Evaluate a password
Select an option (1 or 2): 2
Enter your password to evaluate: p@ssW0rD
Password Strength: Strong
```

## Architecture

The code is structured to follow **Clean Architecture**, separating different concerns into modular components:

### Core Layers:
1. **Entities Layer**:
   - Includes the `Password` class, which contains business logic related to password handling and strength evaluation.

2. **Use Cases Layer**:
   - Includes the `PasswordGenerator` class, which coordinates the password generation process.

3. **Interface Adapters Layer**:
   - Provides the **CLI (Command Line Interface)** that enables interaction with the user.

The following diagram represents the basic layer structure:

```
password-generator/
├── entities/
│   └── password.py            # Password logic and strength evaluation
├── use_cases/
│   └── password_generator.py  # Password generation logic
├── interface_adapters/
│   └── cli.py                 # Command-line interface for interaction
├── run.py                     # Entry point for the CLI app
└── README.md                  # This file
```



Feel free to open issues, contribute, or make pull requests for improvements.

