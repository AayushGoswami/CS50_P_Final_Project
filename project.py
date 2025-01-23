import random
import pyfiglet
import re


def main():
    # Print ASCII art with a random font
    print_ascii_art("CryptograPy50", random.choice(
        ['standard', 'big', 'slant', 'small', 'smscript', 'smshadow', 'smslant', 'speed', 'starwars', 'term']))

    while True:
        print("\n\t\t\033[1mWelcome to CryptograPy50\033[0m\n\n Choose an option below: \n\n 1. Encrypt a text \n 2. Decrypt a text \n 3. Exit\n")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            text = input("\nEnter the text to encrypt: ")
            # Generate a key
            key = generate_key()
            # Split the text unevenly based on the key
            final = split_uneven(text, key)
            # Encrypt the text
            encrypted_text = []
            for part in final:
                encrypted_text.append(encryption_rule(part, key))
            # print(encrypted_text)
            print("\nThe Encrypted text is: \n\n\t\t" +
                  "\033[1m" + str(key)[2::-1] + ''.join(encrypted_text) + str(key)[3:] + "\033[0m")

        elif choice == '2':
            encrypted_text = input("\nEnter the encrypted text: ")
            if re.match(r'^\d{3}.*\d{2}$', encrypted_text) is None:
                print("Invalid encrypted text. Please try again.\n")
                continue
            # Extract the key and text from the encrypted text
            key = (encrypted_text[0:3][::-1] + encrypted_text[-2:])
            text = encrypted_text[3:-2]
            # print("The key is: " + str(key))
            # print("The text is: " + text)
            # Split the text unevenly based on the key
            final = split_uneven(text, key)
            # Decrypt the text
            decrypted_text = []
            for part in final:
                decrypted_text.append(decryption_rule(part, key))
            # print(decrypted_text)
            print("\nThe Decrypted text is: \n\n\t\t" +
                  "\033[1m" + ''.join(decrypted_text) + "\033[0m")

        elif choice == '3':
            print("\n\t\tExiting... \033[1mSee ya later!\033[0m\n")
            break

        else:
            print("Invalid choice. Please try again.\n")
            continue


def print_ascii_art(text, font="standard"):
    # Generate and print ASCII art using the specified font
    ascii_art = pyfiglet.figlet_format(text, font=font)
    print(ascii_art)


def generate_key():
    # Generate a random key and validate it
    key = random.randint(10000, 99999)
    return validate_key(key)


def validate_key(key):
    # Convert key to string and check if it contains '0'
    key = str(key)
    if '0' in key:
        #Key contains 0. Generating new key.
        return generate_key()
    return key


def split_uneven(text, key):
    result = []
    index = 0
    length = len(text)

    while index < length:
        # Alternate between lengths of key[0] and key[2]
        if len(result) % 2 == 0:
            part_length = int(key[0])
        else:
            part_length = int(key[2])

        # Extract the part and append to result
        result.append(text[index:index + part_length])
        index += part_length

    return result


def encryption_rule(text, key):
    encrypted_text = []
    if len(text) == int(key[0]):
        # Encrypt the text using the first rule
        for char in text:
            encrypted_text.append(chr(ord(char) + int(key[1])))
    elif len(text) == int(key[2]):
        # Encrypt the text using the second rule
        for char in text:
            encrypted_text.append(chr(ord(char) + int(key[3])))
    else:
        # Encrypt the text using the default rule
        for char in text:
            encrypted_text.append(chr(ord(char) + int(key[4])))

    return ''.join(encrypted_text)


def decryption_rule(text, key):
    decrypted_text = []
    if len(text) == int(key[0]):
        # Decrypt the text using the first rule
        for char in text:
            decrypted_text.append(chr(ord(char) - int(key[1])))
    elif len(text) == int(key[2]):
        # Decrypt the text using the second rule
        for char in text:
            decrypted_text.append(chr(ord(char) - int(key[3])))
    else:
        # Decrypt the text using the default rule
        for char in text:
            decrypted_text.append(chr(ord(char) - int(key[4])))

    return ''.join(decrypted_text)


# Example Usage
if __name__ == "__main__":
    main()
