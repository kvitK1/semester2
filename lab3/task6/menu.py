'''module to create the menu of notebook'''

from sys import exit as ex
from notebook import Notebook


class Menu:
    '''Display a menu and respond to choices when run.

    Attributes:
        notebook: Notebook
            example of class
        choices: dict
            dict wit options
    '''

    def __init__(self):
        '''Inits Menu with notebook, choices.'''
        self.notebook = Notebook()
        self.choices = {
                "1": self.show_notes,
                "2": self.add_note,
                "3": self.modify_note,
                "4": self.search_notes,
                "5": self.delete_notes,
                "6": self.quit
            }

    def display_menu(self):
        '''Dispplaus the initial message.'''
        print("""
Notebook Menu
1. Show all Notes
2. Add Note
3. Modify Note
4. Search Notes
5. Delete Note
6. Quit """)

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")

    def show_notes(self, notes=None):
        '''Shows the note and what it contains.'''
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f"{note.id}: {note.tags}\n{note.memo}")

    def search_notes(self):
        '''Searches for notes with a certain word.'''
        filt = input("Search for: ")
        notes = self.notebook.search(filt)
        if notes:
            self.show_notes(notes)
        else:
            print(f"Searching for [{filt}] in your notebook gave no results.")

    def add_note(self):
        '''Adds new notes.'''
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        self.notebook.new_note(memo, tags)
        print("Your note has been added.")

    def modify_note(self):
        '''Modifies the note.'''
        i_d = input("Enter a note id: ")
        notes=Notebook().notes
        bol = False
        for note in notes:
            if note.id == i_d:
                bol = True
        if bol:
            memo = input("Enter a memo: ")
            tags = input("Enter tags: ")
            if memo:
                self.notebook.modify_memo(i_d, memo)
            if tags:
                self.notebook.modify_tags(i_d, tags)
            print("Modifications ended.")
        else:
            print("No notes with such id to modify.")

    def delete_notes(self):
        '''Deletes the note.'''
        notes = self.notebook.notes
        note_id = input("Enter a note id: ")
        if notes:
            dec = self.notebook.delete_note(note_id)
            if dec:
                print("Your note has been deleted.")

    @staticmethod
    def quit():
        '''Ends working with notebook.'''
        print("Thank you for using your notebook today.")
        ex(0)

if __name__ == "__main__":
    Menu().run()
