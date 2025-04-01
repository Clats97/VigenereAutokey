# VigenereAutokey
This is the Autokey variant of the Vigenere cipher, which is much more secure and resistant to decryption without the keyword.

---

# Autokey Cipher Tool

## Overview

This Python script provides a simple command-line tool for encrypting and decrypting text using an autokey cipher. It clears the screen, displays an ASCII banner, and offers encryption and decryption options.

## Features

- **Cross-Platform Screen Clearing:**  
  Clears the terminal using `cls` (Windows) or `clear` (Unix-based systems).

- **Interactive Home Screen:**  
  Displays an ASCII art banner and options to either encrypt or decrypt text.

- **Autokey Cipher Implementation:**  
  - **Encryption:** Combines a keyword with the plaintext to generate an effective key, then shifts each letter accordingly.
  - **Decryption:** Uses the provided keyword and appends decrypted characters to reconstruct the key.

- **Input Validation:**  
  Ensures both the text and keyword contain alphabetic characters.

## Function Descriptions

- **`clear_screen()`:** Clears the terminal screen.
- **`print_home_screen()`:** Displays the ASCII art banner and menu.
- **`encrypt(text, keyword)`:** Encrypts text by shifting letters using an autokey method.
- **`decrypt(cipher_text, keyword)`:** Decrypts text by reversing the autokey shift.
- **`process_encrypt()` / `process_decrypt()`:** Handle user input and call the respective functions.
- **`main()`:** Runs the main loop, presenting the home screen and processing user choices.

## Usage

1. **Requirements:**  
   - Python 3.x is required.

2. **Running the Script:**  
   Execute the script in your terminal:
   python scriptname.py
   Replace `scriptname.py` with the actual filename.
   Or, download it directly from Github

4. **Operation:**  
   - The script clears the screen and displays a menu.
   - Choose **1** to encrypt or **2** to decrypt.
   - Follow the prompts to input text and a keyword.
