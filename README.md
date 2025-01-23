# __CryptograPy50__

#### Video Demo:  <[CS50P Final Project Submission](https://youtu.be/D3yUFykZOW0)>

## Description:

A Python-based text encryption and decryption tool that implements a unique encryption algorithm using dynamic key generation and uneven text splitting.

## Features

- Custom encryption/decryption algorithm
- Dynamic key generation
- ASCII art display using multiple fonts
- Interactive command-line interface
- Uneven text splitting for enhanced security
- Colorized output for better user experience

## Requirements

- Python 3.10 or later
- pyfiglet library (`pip install pyfiglet`)
- random module (built-in)
- re (RegEx) module (`pip install regex`)

## Usage

Run the program using Python:
```bash
python project.py
```

The program offers three main options:
1. Encrypt a text
2. Decrypt a text
3. Exit

### Encryption Process

1. Enter the text you want to encrypt when prompted
2. The program will:
   - Generate a unique 5-digit key (without zeros)
   - Split your text unevenly based on the key
   - Apply different encryption rules to each part
   - Return the encrypted text with the key embedded

### Decryption Process

1. Enter the encrypted text (including the embedded key)
2. The program will:
   - Extract the key from the encrypted text
   - Split the text using the same algorithm
   - Apply corresponding decryption rules
   - Return the original text

## How It Works

### Key Generation
- Generates a random 5-digit key between 10000-99999
- Validates that the key doesn't contain zeros
- Uses different digits of the key for various encryption operations

### Text Splitting Algorithm
The `split_uneven()` function splits the input text into parts based on the key:
- Let te key be in the form of **'xaybc'**
- The first **x** number of characters are split and grouped togehter, then the next **y** number of characters are split and grouped together, and so on
- This pattern contnues till the end of the string

### Encryption Rules
Different encryption rules are applied based on the length of text segments:
- If length matches first key digit: shifts characters by second key digit, based on the ASCII values of the characters
- If length matches third key digit: shifts characters by fourth key digit, based on the ASCII values of the characters
- Otherwise: shifts characters by fifth key digit, based on the ASCII values of the characters

### Security Features
- Uneven text splitting makes pattern recognition more difficult
- Key embedding within encrypted text ensures key transmission
- Multiple encryption rules based on segment length
- No zero digits in keys to prevent padding issues

## Functions

### `print_ascii_art(text, font="standard")`
Generates ASCII art banner using the specified font

### `generate_key()`
Creates and validates a random 5-digit encryption key

### `validate_key(key)`
Ensures the key doesn't contain zeros

### `split_uneven(text, key)`
Splits input text into uneven segments based on key digits

### `encryption_rule(text, key)`
Applies encryption rules based on text length and key digits

### `decryption_rule(text, key)`
Reverses the encryption process using the same key

## Example

## Limitations

- The encryption strength depends on the randomness of the key generation
- Not suitable for encrypting very large text blocks
- The embedded key slightly increases the output length

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- pyfiglet library for ASCII art generation
- Inspired by classic substitution ciphers
- Developed as part of an educational project
