from Crypto.Cipher import DES3
import base64

def decrypt_text(key, encrypted_text, iv):
    ciphertext = base64.b64decode(encrypted_text)
    iv = base64.b64decode(iv)

    # Create TripleDES cipher object
    cipher = DES3.new(key, DES3.MODE_CBC, iv)

    decrypted_text = cipher.decrypt(ciphertext)

    decrypted_text = decrypted_text[:-ord(decrypted_text[-1])]

    return decrypted_text.decode('utf-8')

if __name__ == "__main__":
    key = b'mysecretpassword'  # Replace with the same key used for encryption
    encrypted_text = '...'  
    iv = '...'  

    decrypted_text = decrypt_text(key, encrypted_text, iv)
    print(f"Decrypted text: {decrypted_text}")
