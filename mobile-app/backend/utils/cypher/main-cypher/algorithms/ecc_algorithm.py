"""

"""

# Libraries
from cryptography.hazmat.primitives.asymmetric import ec, utils, x25519
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.kdf.hkdf import HKDFExpand
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from .aes_algorithm import encrypt_data, decrypt_data


# Constants and global variables
PRIVATE_KEY_PATH = 'x25519_private_key.pem'
PUBLIC_KEY_PATH = 'x25519_public_key.pem'


# Functions
def generate_key_pair():
    """
    Generates a key pair using the x25519 elliptic curve algorithm.

    Returns:
        tuple: A tuple containing the private key and public key.
    """
    private_key = x25519.X25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key


def share_public_key(private_key, public_key):
    """
    Shares the public key with another peer.
    """
    # When connecting to another par, share the public key.
    return private_key.exchange(public_key)


def generate_shared_key(private_key, public_shared_key):
    """
    Generates a shared key using the provided private key and public shared key.

    Parameters:
        private_key: The private key used for generating the shared key.
        public_shared_key: The public shared key used for generating the shared key.

    Returns:
        The generated shared key.

    """
    return private_key.exchange(public_shared_key)


def generate_session_key(private_key, public_shared_key, info=b'handshake data'):
    """
    Generates a session key using the provided private key and public shared key.

    Parameters:
        private_key: The private key used for key generation.
        public_shared_key: The public shared key used for key generation.
        info: Additional information used as input to the key derivation function. Default is b'handshake data'.

    Returns:
        The derived session key.

    """
    shared_key = generate_shared_key(private_key, public_shared_key)
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=info,
    ).derive(shared_key)
    return derived_key


def save_key_pair(file_private_key, file_public_key, private_key, public_key):
    """
    Save the private and public key pair to files.

    Parameters:
        private_key (cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePrivateKey): The private key.
        public_key (cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePublicKey): The public key.
    """
    with open(file_private_key, 'wb') as file:
        file.write(private_key.private_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PrivateFormat.Raw,
            encryption_algorithm=serialization.NoEncryption()
        ))

    with open(file_public_key, 'wb') as file:
        file.write(public_key.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw,
        ))


def load_key_pair(file_private_key, file_public_key):
    """
    Load the private and public key pair from the specified paths.

    Returns:
        tuple: A tuple containing the private key and public key.
    """
    try:
        with open(file_private_key, 'rb') as file:
            private_key = x25519.X25519PrivateKey.from_private_bytes(file.read())
   
        with open(file_public_key, 'rb') as file:
            public_key = x25519.X25519PublicKey.from_public_bytes(file.read())

        return private_key, public_key
    except FileNotFoundError:
        raise FileNotFoundError('Key pair not found.')


def load_or_generate_key_pair(file_private_key, file_public_key):
    """
    Loads or generates a key pair for encryption.

    This function first tries to load a previously generated key pair from a file.
    If the file is not found, it generates a new key pair and saves it to the file.
    The generated or loaded key pair is then returned.

    Returns:
        tuple: A tuple containing the public and private keys.

    Raises:
        FileNotFoundError: If the file containing the key pair is not found.
    """
    try:
        return load_key_pair(file_private_key, file_public_key)
    except FileNotFoundError:
        generate_key_pair()
        return load_key_pair(file_private_key, file_public_key)
