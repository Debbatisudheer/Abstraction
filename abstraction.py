from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def encrypt_message(message, password):
    # Derive a key from the password using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=b'salt_123',
        iterations=100000,
        length=32,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    # Generate a random initialization vector (IV)
    iv = b'random_iv_456'

    # Create a cipher object with AES-GCM mode
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the message
    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()

    # Get the authentication tag
    tag = encryptor.tag

    return (ciphertext, iv, tag)

def decrypt_message(ciphertext, iv, tag, password):
    # Derive the key from the password using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=b'salt_123',
        iterations=100000,
        length=32,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    # Create a cipher object with AES-GCM mode
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the message
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()

    return decrypted_message.decode()

# Example usage
message = "Hi Sudheer"
password = "secure_password"

# Encryption
ciphertext, iv, tag = encrypt_message(message, password)

# Decryption
decrypted_message = decrypt_message(ciphertext, iv, tag, password)

print(f"Original Message: {message}")
print(f"Encrypted Message: {ciphertext}")
print(f"Decrypted Message: {decrypted_message}")