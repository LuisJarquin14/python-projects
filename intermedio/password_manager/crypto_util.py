from cryptography.fernet import Fernet

# Generar y guardar una clave
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt(message):
    return cipher_suite.encrypt(message.encode())

def decrypt(encrypted_message):
    return cipher_suite.decrypt(encrypted_message).decode()