from typing import Dict

from authentication_authorization_system.exceptions import InvalidPassword
from authentication_authorization_system.exceptions import InvalidUsername
from authentication_authorization_system.exceptions import NotLoggedInError
from authentication_authorization_system.exceptions import NotPermittedError
from authentication_authorization_system.exceptions import PasswordTooShort
from authentication_authorization_system.exceptions import UsernameAlreadyExists
from authentication_authorization_system.user import User


class Authenticator:
    """Maps usernames to user objects"""

    def __init__(self):
        self.users: Dict[str, User] = {}

    def add_user(self, username: str, password: str):
        if username in self.users:
            raise UsernameAlreadyExists
        if len(password) < 6:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def login(self, username: str, password: str):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True
        return True

    def is_logged_in(self, username: str):
        if username in self.users:
            return self.users[username].is_logged_in
        return False


class Authorizor:
    """Maps permissions to users"""

    def __init__(self, authenticator: Authenticator):
        self.authenticator = authenticator
        self.permissions: Dict = {}

    def add_permission(self, perm_name: str):
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission already exists")

    def permit_user(self, perm_name: str, username: str):
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)

    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)

        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True


authenticator = Authenticator()
authorizor = Authorizor(authenticator)
