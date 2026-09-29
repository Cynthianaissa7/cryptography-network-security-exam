import sys
import os
import hashlib
from cryptography.fernet import Fernet, InvalidToken

def generate_and_save_key(key_filepath):
    """Generates a key and saves it outside the repository."""
    key = Fernet.generate_key()
    with open(key_filepath, 'wb') as key_file:
        key_file.write(key)
    print(f"[+] New key generated and saved to '{key_filepath}'.")

def load_key(key_filepath):
    """Loads the encryption key from a local file path."""
    if not os.path.exists(key_filepath):
        raise FileNotFoundError(f"Key file not found at '{key_filepath}'.")
    with open(key_filepath, 'rb') as key_file:
        return key_file.read()

def encrypt_file(input_filepath, output_filepath, key_filepath):
    """Encrypts a file using Fernet (AES)."""
    try:
        key = load_key(key_filepath)
        fernet = Fernet(key)
        
        with open(input_filepath, 'rb') as f:
            data = f.read()
            
        encrypted_data = fernet.encrypt(data)
        
        with open(output_filepath, 'wb') as f:
            f.write(encrypted_data)
            
        print(f"[+] File successfully encrypted and saved to '{output_filepath}'.")
    except FileNotFoundError as e:
        print(f"[-] Error: {e}")
    except Exception as e:
        print(f"[-] An error occurred during encryption: {e}")

def decrypt_file(input_filepath, output_filepath, key_filepath):
    """Decrypts a file using Fernet (AES)."""
    try:
        key = load_key(key_filepath)
        fernet = Fernet(key)
        
        with open(input_filepath, 'rb') as f:
            encrypted_data = f.read()
            
        decrypted_data = fernet.decrypt(encrypted_data)
        
        with open(output_filepath, 'wb') as f:
            f.write(decrypted_data)
            
        print(f"[+] File successfully decrypted and saved to '{output_filepath}'.")
    except FileNotFoundError as e:
        print(f"[-] Error: {e}")
    except InvalidToken:
        print("[-] Error: Decryption failed. Invalid key or corrupted file.")
    except Exception as e:
        print(f"[-] An error occurred during decryption: {e}")

def calculate_sha256(filepath):
    """Calculates and returns the SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"[-] Error: File '{filepath}' not found.")
        return None
    except Exception as e:
        print(f"[-] Error calculating hash: {e}")
        return None

def verify_integrity(original_hash, target_filepath):
    """Checks whether the file matches the expected original hash."""
    current_hash = calculate_sha256(target_filepath)
    if current_hash is None:
        return
    print(f"Expected Hash: {original_hash}")
    print(f"Current Hash:  {current_hash}")
    if original_hash == current_hash:
        print("[+] Integrity Verification Passed: File is untouched.")
    else:
        print("[-] Integrity Verification Failed: File has been modified or corrupted!")

if __name__ == "__main__":
    # Demonstration Workflow
    key_path = "../secret.key"  # Stored outside repository folder
    sample_file = "sample_student_records.csv"
    enc_file = "sample_student_records.csv.enc"
    dec_file = "sample_student_records_decrypted.csv"

    # Create dummy sample file if not present
    if not os.path.exists(sample_file):
        with open(sample_file, "w") as f:
            f.write("StudentID,Name,Department,GPA\nS101,John Doe,CS,3.8\nS102,Jane Smith,IT,3.9\n")

    # Generate key if missing
    if not os.path.exists(key_path):
        generate_and_save_key(key_path)

    print("\n--- 1. ENCRYPTION ---")
    encrypt_file(sample_file, enc_file, key_path)

    print("\n--- 2. DECRYPTION ---")
    decrypt_file(enc_file, dec_file, key_path)

    print("\n--- 3. INTEGRITY CHECK (SHA-256) ---")
    orig_hash = calculate_sha256(sample_file)
    print(f"Original File Hash: {orig_hash}")
    verify_integrity(orig_hash, dec_file)

    print("\n--- 4. ERROR HANDLING TESTS ---")
    print("Testing missing file:")
    decrypt_file("non_existent_file.enc", "out.txt", key_path)
    
    print("\nTesting corrupted file decryption:")
    with open("corrupted.enc", "wb") as f:
        f.write(b"InvalidEncryptedDataPayload")
    decrypt_file("corrupted.enc", "out.txt", key_path)
    if os.path.exists("corrupted.enc"):
        os.remove("corrupted.enc")
