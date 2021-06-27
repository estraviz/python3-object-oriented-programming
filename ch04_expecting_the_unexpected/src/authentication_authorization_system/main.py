from authentication_authorization_system import auth


class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login,
            "test": self.test,
            "change": self.change,
            "quit": self.quit,
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = auth.authenticator.login(username, password)
            except auth.InvalidUsername:
                print(f"Error: username '{username}' does not exist")
            except auth.InvalidPassword:
                print(f"Error: incorrect password")
            else:
                self.username = username

    def is_permitted(self, permission):
        try:
            auth.authorizor.check_permission(permission, self.username)
        except auth.NotLoggedInError as e:
            print(f"'{e.username}' user is not logged in")
        except auth.NotPermittedError as e:
            print(f"'{e.username}' not allowed to {permission}")
            return False
        else:
            return True

    def test(self):
        if self.is_permitted("test_program"):
            print("Testing program in progress!")

    def change(self):
        if self.is_permitted("change_program"):
            print("Changing program in progress!")

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                print("""
                Please enter a command:
                \tlogin\tLogin
                \ttest\tTest the program
                \tchange\tChange the program
                \tquit\tQuit
                """)
                answer = input("Enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print(f"'{answer}' is not a valid option")
                else:
                    func()
        finally:
            print("Thank you for using the auth module!")


if __name__ == '__main__':
    auth.authenticator.add_user("javier", "javierpassword")
    auth.authorizor.add_permission("test_program")
    auth.authorizor.add_permission("change_program")
    auth.authorizor.permit_user("test_program", "javier")
    Editor().menu()
