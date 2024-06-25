# TripleDES Encryption and Decryption


## Usage Scenario: Protecting Sensitive Data

Imagine you work for an organization handling sensitive data such as financial or medical information. To secure this data during storage or transmission, the organization should employ robust encryption algorithms like TripleDES.

### Problem

A file containing sensitive data has been encrypted using TripleDES and base64 before being stored in a database. Now, a security analyst needs to access and analyze this data to investigate a potential anomaly in the records.

### Solution

Using the provided `decrypt.py` script in this repository:

1. **Setup**: The analyst sets up the environment with the appropriate encryption key and retrieves the base64-encoded cipher text from the file or database.

2. **Decryption**: They run the `decrypt.py` script, providing the encryption key and base64-encoded cipher text as input.

3. **Outcome**: The script decrypts the cipher text using the TripleDES algorithm and decodes the output, granting the analyst access to the original plaintext.

### Benefits

- **Security**: Enables controlled access to sensitive data only to authorized personnel.
- **Compliance**: Facilitates compliance with data protection regulations by employing strong encryption.
- **Agile Investigation**: Speeds up incident response by quickly recovering and analyzing encrypted data.

This scenario demonstrates how the `decrypt.py` script can be effectively used in an enterprise environment to ensure data security and integrity using TripleDES.

### Description

The `decrypt.py` script demonstrates how to decrypt data that has been encrypted using TripleDES. It uses the `Crypto.Cipher.DES3` module for decryption and `base64` for decoding the encrypted data.

### Usage

To use the `decrypt.py` script, follow these steps:

1. Replace `"mysecretencryptionkey"` with your actual encryption key.
2. Replace `"BASE64_ENCODED_ENCRYPTED_TEXT_HERE"` with your actual base64 encoded encrypted text.

### Example

```python
from Crypto.Cipher import DES3
import base64

def decrypt_data(key, data):
    # Decode the base64 encoded data
    encrypted_data = base64.b64decode(data)

    # Create a TripleDES cipher object
    cipher = DES3.new(key.encode(), DES3.MODE_ECB)

    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Return the decrypted data
    return decrypted_data.decode()

# Example usage
if __name__ == "__main__":
 
    encryption_key = "mysecretencryptionkey"
    encrypted_text = "BASE64_ENCODED_ENCRYPTED_TEXT_HERE" 

    decrypted_text = decrypt_data(encryption_key, encrypted_text)
    print("Decrypted Text:", decrypted_text)

Replace "mysecretencryptionkey" and "BASE64_ENCODED_ENCRYPTED_TEXT_HERE" with your actual encryption key and encrypted text respectively when you use this script. Ensure that the data you are decrypting was originally encrypted using TripleDES and encoded in base64.