"""

"""

# Libraries
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


# Functions
def encrypt_data(session_key, data, iv):
    """
    Encrypts the given data using the AES algorithm.

    Parameters:
        session_key (bytes): The session key used for encryption.
        data (str): The data to be encrypted.
        iv (bytes): The initialization vector used for encryption.

    Returns:
        bytes: The encrypted data.
    """
    cipher = Cipher(algorithms.AES(session_key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data.encode('utf-8')) + encryptor.finalize()
    return encrypted_data


def decrypt_data(session_key, encrypted_data, iv):
    """
    Decrypts the given encrypted data using the provided session key and initialization vector (IV).

    Parameters:
        session_key (bytes): The session key used for decryption.
        encrypted_data (bytes): The data to be decrypted.
        iv (bytes): The initialization vector used for decryption.

    Returns:
        str: The decrypted data as a string.
    """
    cipher = Cipher(algorithms.AES(session_key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    return decrypted_data.decode('utf-8')
