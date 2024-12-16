# Password Generator and Strength Checker

This project is a Python-based tool that allows users to generate secure passwords and evaluate the strength of their passwords based on various criteria.

## Features

1. **Password Generation**:
   - Generate random passwords of customizable length.
   - Optionally include uppercase letters, lowercase letters, numbers, and symbols.

2. **Password Strength Evaluation**:
   - Evaluate the strength of a given password.
   - Provide feedback on whether the password is `Weak`, `Moderate`, or `Strong`.

3. **Common Password Weakness Detection**:
   - Detect patterns such as repeated characters, sequential characters, and known weak passwords.
   - Avoid common weak words like `password` or `admin`.

---

## How to Use

### Requirements
- Python 3.8 or later

### Run the Tool

1. Clone the repository or copy the script file to your local machine.
2. Open a terminal and navigate to the directory containing the script.
3. Run the following command:
   ```bash
   python password_generator.py
   ```

### Options
When running the script, you will be presented with two options:
1. **Generate a password**: The script will generate a random password based on pre-defined settings.
2. **Evaluate a password**: The script will analyze and score a user-provided password.

---

## Password Strength Criteria

The password's strength is evaluated based on the following:

1. **Length**:
   - Minimum of 8 characters for a base score.
   - Additional points for passwords 12 characters or longer.

2. **Character Diversity**:
   - Presence of uppercase letters, lowercase letters, digits, and special symbols.

3. **Avoid Weak Patterns**:
   - Detection of repeated characters (e.g., `aaa`).
   - Avoidance of sequential characters (e.g., `1234` or `abcd`).
   - Detection of known weak passwords or words (e.g., `password`, `admin`, `welcome`).

The final strength is determined as follows:
- **Weak**: Total score of 3 or less.
- **Moderate**: Total score of 4 to 5.
- **Strong**: Total score of 6 or higher.

---

## Example

### Generating a Password

```plaintext
$ python password_generator.py
1. Generate a password
2. Evaluate a password
Select an option (1 or 2): 1
Generated Password: q1W$8z@N&f
Password Strength: Strong
```

### Evaluating a Password

```plaintext
$ python password_generator.py
1. Generate a password
2. Evaluate a password
Select an option (1 or 2): 2
Enter your password to evaluate: MyPa$$w0rd123
Password Strength: Strong
```

---

## Future Enhancements

- Add a configuration file to customize password generation settings persistently.
- Enhance the password strength evaluation with more sophisticated algorithms.
- Include a database of weak passwords to improve detection.
- Add a graphical user interface (GUI).

---

## License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## Contributions
Contributions are welcome! Please submit issues or pull requests to enhance the functionality of the tool.

---

## Acknowledgments
This project is inspired by the need for secure password practices and the importance of raising awareness about password vulnerabilities.

