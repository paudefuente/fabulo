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
        private_key, public_key = generate_key_pair()
        print("Key pair generated and saved.")

    if function == "share_public_key":
        private_key, public_key = sys.argv[2], sys.argv[3]

        # Share public key
        shared_key = share_public_key(private_key, public_key)
        print("Public key shared.")

    if function == "generate_session_key":
        private_key, public_shared_key = sys.argv[2], sys.argv[3]

        # Generate session key
        session_key = generate_session_key(private_key, public_shared_key)
        print("Session key:", session_key)

    if function == "save_key_pair":
        private_key, public_key = sys.argv[2], sys.argv[3]

        # Save key pair
        save_key_pair(PRIVATE_KEY_PATH, PUBLIC_KEY_PATH, private_key, public_key)
        print("Key pair saved.")

    if function == "load_key_pair":
        # Load key pair
        private_key, public_key = load_key_pair(PRIVATE_KEY_PATH, PUBLIC_KEY_PATH)
        print("Key pair loaded.")

    if function == "encrypt":
        session_key, iv, data = sys.argv[2], sys.argv[3], sys.argv[4]

        # Perform encryption
        ciphertext = encrypt_data(session_key, iv, data)
        print("Data encrypted.")

    if function == "decrypt":
        session_key, iv, data = sys.argv[2], sys.argv[3], sys.argv[4]

        # Perform decryption
        plaintext = decrypt_data(session_key, iv, data)
        print("Data decrypted.")
    else:
        print("Invalid function.")
