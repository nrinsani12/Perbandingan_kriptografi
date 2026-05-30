from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time

# DATA
plaintext = "Nur insani"

print("Plaintext :", plaintext)
print("-" * 50)

# 1. KRIPTOGRAFI SIMETRIS (AES/Fernet)
print("KRIPTOGRAFI SIMETRIS (AES/Fernet)")

# Generate key
fernet_key = Fernet.generate_key()
cipher_fernet = Fernet(fernet_key)

# Enkripsi
start_encrypt = time.time()
ciphertext_fernet = cipher_fernet.encrypt(plaintext.encode())
end_encrypt = time.time()

# Dekripsi
start_decrypt = time.time()
decrypted_fernet = cipher_fernet.decrypt(ciphertext_fernet).decode()
end_decrypt = time.time()

# Hasil
print("Ciphertext :", ciphertext_fernet)
print("Hasil Dekripsi :", decrypted_fernet)

fernet_encrypt_time = end_encrypt - start_encrypt
fernet_decrypt_time = end_decrypt - start_decrypt

print("Waktu Enkripsi :", fernet_encrypt_time, "detik")
print("Waktu Dekripsi :", fernet_decrypt_time, "detik")
print("Ukuran Ciphertext :", len(ciphertext_fernet), "byte")

print("-" * 50)

# 2. KRIPTOGRAFI ASIMETRIS (RSA)
print("KRIPTOGRAFI ASIMETRIS (RSA)")

# Generate key RSA
rsa_key = RSA.generate(2048)
private_key = rsa_key
public_key = rsa_key.publickey()

cipher_rsa_encrypt = PKCS1_OAEP.new(public_key)
cipher_rsa_decrypt = PKCS1_OAEP.new(private_key)

# Enkripsi
start_encrypt_rsa = time.time()
ciphertext_rsa = cipher_rsa_encrypt.encrypt(plaintext.encode())
end_encrypt_rsa = time.time()

# Dekripsi
start_decrypt_rsa = time.time()
decrypted_rsa = cipher_rsa_decrypt.decrypt(ciphertext_rsa).decode()
end_decrypt_rsa = time.time()

# Hasil
print("Ciphertext :", ciphertext_rsa)
print("Hasil Dekripsi :", decrypted_rsa)

rsa_encrypt_time = end_encrypt_rsa - start_encrypt_rsa
rsa_decrypt_time = end_decrypt_rsa - start_decrypt_rsa

print("Waktu Enkripsi :", rsa_encrypt_time, "detik")
print("Waktu Dekripsi :", rsa_decrypt_time, "detik")
print("Ukuran Ciphertext :", len(ciphertext_rsa), "byte")