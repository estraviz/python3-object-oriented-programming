import hashlib


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password: str):
        hash_string = self.username + password
        hash_bytes = hash_string.encode('utf-8')
        return hashlib.sha256(hash_bytes).hexdigest()

    def check_password(self, password: str):
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password
