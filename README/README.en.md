# Encrypt

A custom encryption system in Python that uses a transposition matrix to encode and verify passwords. Ideal for exploring basic security concepts and programming logic.

# Custom Encryption System in Python

This project implements a custom encryption system, developed as a hands-on approach to explore logic and information security concepts. The algorithm uses a transposition matrix of characters to encode and verify passwords, providing a detailed view of how basic encryption mechanisms work.

Although this system is not intended for production use, it demonstrates the fundamentals of cryptographic operations, string manipulation, and programming logic.

## Features
- **Custom Encoding:** Creates an encrypted password from a combination of the password and encoder provided by the user.  
- **Password Verification:** Allows authentication by comparing the entered password with the stored encrypted value.  
- **Password Change:** Includes the option to reset the encrypted password and test its validity.

## Technical Details
1. The password and encoder provided by the user are processed to ensure their sizes align.  
2. A transposition matrix is generated to map the characters.  
3. The password is encoded using the matrix and stored in a text file (`senha.txt`).  
4. The system allows the password to be dynamically changed and tested.

## Initial Setup
- **Default Password:** `12345`  
- **Default Encoder:** `teste`

These values can be modified directly in the system when running the script.

## Disclaimer
This system is not designed for production applications or the storage of sensitive information. For real projects, it is recommended to use libraries such as `hashlib` for robust algorithms like SHA-256 or bcrypt. This project aims to demonstrate the fundamental concepts of encryption and applied logic.

## How to Use
1. Clone this repository.  
2. Run the `codification.py` script.  
3. Follow the instructions in the terminal to encode, verify, or reset passwords.

## Contributions
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an *issue* or submit a *pull request*.
