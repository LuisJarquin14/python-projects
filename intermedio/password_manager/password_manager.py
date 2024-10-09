from crypto_util import encrypt, decrypt

class PasswordManager:
    def __init__(self):
        self.passwords = {}
        
    def add_password(self, site, username, password):
        encrypted_password = encrypt(password)
        self.passwords[site] = (username, encrypted_password)
        
    def get_password(self, site):
        if site in self.passwords:
            username, encrypted_password = self.passwords[site]
            return username, decrypt(encrypted_password)
        return None
    
    def delete_password(self, site):
        if site in self.passwords:
            del self.passwords[site]
            
    def get_all_passwords(self):
        return {site: (username, decrypt(pwd)) for site, (username, pwd) in self.passwords.items()}