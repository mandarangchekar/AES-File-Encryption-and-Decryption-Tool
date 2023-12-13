from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os

class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data, AES.block_size))
        iv = cipher.iv
        return iv + ct_bytes

    def decrypt(self, data):
        iv = data[:AES.block_size]
        ct = data[AES.block_size:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        try:
            pt = unpad(cipher.decrypt(ct), AES.block_size)
            return pt
        except ValueError as e:
            raise ValueError("Incorrect decryption key or corrupted data")

def encrypt_file(filename):
    key = get_random_bytes(16)
    aes = AESCipher(key)
    try:
        with open(filename, 'rb') as f:
            original_data = f.read()

        encrypted_data = aes.encrypt(original_data)

        encrypted_file_name = 'encrypted_' + filename
        with open(encrypted_file_name, 'wb') as f:
            f.write(encrypted_data)

        with open(filename + '.key', 'wb') as f:
            f.write(key)

        print(f"Encryption of {filename} is done successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_file(filename, key_file):
    try:
        with open(key_file, 'rb') as f:
            key = f.read()

        aes = AESCipher(key)

        with open(filename, 'rb') as f:
            encrypted_data = f.read()

        decrypted_data = aes.decrypt(encrypted_data)

        decrypted_file_name = 'decrypted_' + filename.replace('encrypted_', '')
        with open(decrypted_file_name, 'wb') as f:
            f.write(decrypted_data)

        print(f"Decryption of {filename} is done successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        # ANSI escape codes to set text color
        red = "\033[91m"
        green = "\033[92m"
        blue = "\033[94m"
        magenta = "\033[95m"
        cyan = "\033[96m"
        yellow = "\033[93m"
        reset = "\033[0m"  # Reset to default color

        print(f"{magenta}File Encryption and Decryption Tool{reset}")
        print(f"{cyan}---------------------------------{reset}")
        print("Welcome! What would you like to do?")
        print(f"{green}1. Encrypt a File{reset}")
        print(f"{yellow}2. Decrypt a File{reset}")
        print(f"{red}3. Exit{reset}")
        choice = input("Please enter your choice (1, 2, or 3): ")

        if choice == '1':
            print(f"\n{blue}File Encryption{reset}")
            filename = input("Enter the name of the file you want to encrypt: ")
            encrypt_file(filename)
            print(f"{green}The encrypted file and key have been saved in the same directory.{reset}")
        elif choice == '2':
            print(f"\n{blue}File Decryption{reset}")
            filename = input("Enter the name of the encrypted file to decrypt: ")
            key_file = input("Enter the name of the key file: ")
            decrypt_file(filename, key_file)
            print(f"{green}The decrypted file has been saved in the same directory.{reset}")
        elif choice == '3':
            print(f"{red}Thank you for using our tool. Goodbye!{reset}")
            break
        else:
            print(f"{red}Invalid choice. Please enter 1, 2, or 3.{reset}")

if __name__ == "__main__":
    main()
