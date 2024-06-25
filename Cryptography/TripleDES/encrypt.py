from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import base64

def encrypt_text(key, plaintext):
    plaintext = plaintext + ((8 - len(plaintext) % 8) * chr(8 - len(plaintext) % 8))
    iv = get_random_bytes(DES3.block_size)
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext.encode())
    encrypted_text = base64.b64encode(ciphertext).decode('utf-8')
    iv = base64.b64encode(iv).decode('utf-8')

    return encrypted_text, iv

if __name__ == "__main__":
    key = b'mysecretpassword'  # Key must be 16 or 24 bytes long
    plaintext = 'Hello, world!'  # Replace with the text you want to encrypt

    encrypted_text, iv = encrypt_text(key, plaintext)
    print(f"Encrypted text: {encrypted_text}")
    print(f"Initialization vector (IV): {iv}")
