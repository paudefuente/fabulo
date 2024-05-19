"""

"""

# Libraries
from algorithms.aes_algorithm import encrypt_data, decrypt_data
from algorithms.ecc_algorithm import generate_key_pair, share_public_key, save_key_pair, load_key_pair, generate_session_key
import os
import sys


# Constants and global variables
PRIVATE_KEY_PATH = 'x25519_private_key.pem'
PUBLIC_KEY_PATH = 'x25519_public_key.pem'

# Functions 
def generate_iv():
    """
    Generates a random initialization vector (IV) for AES encryption.
    
    Returns:
        bytes: A random 16-byte IV.
    """
    return os.urandom(16)


if __name__ == '__main__':

    # Choose the function to invoke
    function = sys.argv[1]

    if function == "generate_key_pair":
        # Generate key pair
        save_key_pair(PRIVATE_KEY_PATH, PUBLIC_KEY_PATH)
        print("Key pair generated and saved.")

    if function == "share_public_key":
        # Share public key
        public_key = load_key_pair(PUBLIC_KEY_PATH)[1]
        share_public_key(public_key)
        print("Public key shared.")

    if function == "save_key_pair":
        # Save key pair
        save_key_pair(PRIVATE_KEY_PATH, PUBLIC_KEY_PATH)
        print("Key pair saved.")

    if function == "load_key_pair":
        # Load key pair
        private_key, public_key = load_key_pair(PRIVATE_KEY_PATH, PUBLIC_KEY_PATH)
        print("Key pair loaded.")

    if function == "encrypt":
        # Perform encryption
        plaintext = input("Enter the plaintext to encrypt: ")
        iv = generate_iv()
        ciphertext = encrypt_data(plaintext, iv)
        print("Ciphertext:", ciphertext)

    if function == "decrypt":
        # Perform decryption
        ciphertext = input("Enter the ciphertext to decrypt: ")
        iv = input("Enter the initialization vector (IV): ")
        plaintext = decrypt_data(ciphertext, iv)
        return plaintext
    else:
        print("Invalid function.")
    

    if function == "generate_session_key":
        # Generate session key
        session_key = generate_session_key()
        print("Session key:", session_key)
    else:
        print("Invalid function.")