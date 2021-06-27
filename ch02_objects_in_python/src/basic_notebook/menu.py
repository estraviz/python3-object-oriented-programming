import sys
from typing import Callable
from typing import NoReturn

from basic_notebook.notebook import Notebook


class Menu:
    def __init__(self) -> None:
        self.notebook: Notebook = Notebook()
        self.choices: dict = {  # command pattern
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
        }

    def display_menu(self) -> None:
        print("""
        Notebook Menu
        
        1. Show all notes
        2. Search notes
        3. Add note
        4. Modify note
        5. Quit
        """)

    def run(self) -> None:
        while True:
            self.display_menu()
            choice: str = input("Enter an option: ")
            action: Callable = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")

    def show_notes(self, notes=None) -> None:
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f"{note.id}: {note.tags}\n{note.memo}")

    def search_notes(self) -> None:
        filter: str = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self) -> None:
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self) -> None:
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self) -> NoReturn:
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == '__main__':
    Menu().run()
