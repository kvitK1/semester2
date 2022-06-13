"""lab5 task2"""


class Book:
    """A class to represent a book and info about it.

    Attributes
    ------------
        name: str
            title of the book
        author: str
            author of the book
        pages: int
            number of pages in the book
        curr_page: int
            number of the current page in the book (default to 1)
        bookmark: None|int
            number of a bookmarked page in the book (default to None)

    """
    def __init__(self, name, author, pages, curr_page=1, bookmark=None):
        """Inits the Book class with arguments:
            name, author, pages, curr_page, bookmark."""
        self.name = name
        self.author = author
        self.pages = pages
        self.curr_page = curr_page
        self.bookmark = bookmark
    
    def __str__(self):
        """Shows the information about book when printed."""
        str_pages = 'page' if self.pages == 1 else 'pages'
        str_text = f"Book<{self.name} by {self.author}: {self.pages} \
{str_pages}, currently on page {self.curr_page}>"
        if self.bookmark is not None:
            str_text = f"{str_text[:-1]}, page {self.bookmark} bookmarked>"
        return str_text

    def __eq__(self, other):
        """Overrides the __eq__ method."""
        if self.name==other.name and self.curr_page==other.curr_page\
            and self.bookmark==other.bookmark and self.author==other.author\
                and self.pages==other.pages:
            return True
        return False

    def turn_page(self, page):
        """Turns the certain number of pages in the book."""
        self.curr_page += page
        if self.curr_page <= 0:
            self.curr_page = 1
        elif self.curr_page > self.pages:
            self.curr_page = self.pages

    def get_current_page(self):
        """Returns the current page in the book."""
        return self.curr_page

    def place_bookmark(self):
        """Marks the page in the book."""
        self.bookmark = self.curr_page

    def get_bookmarked_page(self):
        """Returns the bookmarked page."""
        return self.bookmark

    def turn_to_bookmark(self):
        """Goes back to the bookmarked page."""
        if self.bookmark is not None:
            self.curr_page = self.bookmark

    def remove_bookmark(self):
        """Removes the bookmark from the book."""
        self.bookmark = None


def test_book_class():
    """Tests the methods of the class Book."""
    print("Testing Book class...", end="")
    # A Book has a title, and author, and a number of pages.
    # It also has a current page, which always starts at 1. There is no page 0!
    book1 = Book("Harry Potter and the Sorcerer's Stone",
                 "J. K. Rowling", 309)
    assert (str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " +
            "J. K. Rowling: 309 pages, currently on page 1>")
    book2 = Book("Carnegie Mellon Motto", "Andrew Carnegie", 1)
    assert (str(book2) == "Book<Carnegie Mellon Motto by Andrew Carnegie: " +
            "1 page, currently on page 1>")

    # You can turn pages in a book. Turning a positive number of pages moves
    # forward; turning a negative number moves backwards. You can't move past
    # the first page going backwards or the last page going forwards
    book1.turn_page(4)  # turning pages does not return
    assert (book1.get_current_page() == 5)
    book1.turn_page(-1)
    assert (book1.get_current_page() == 4)
    book1.turn_page(400)
    assert (book1.get_current_page() == 309)
    assert (str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " +
            "J. K. Rowling: 309 pages, currently on page 309>")
    book2.turn_page(-1)
    assert (book2.get_current_page() == 1)
    book2.turn_page(1)
    assert (book2.get_current_page() == 1)

    # You can also put a bookmark on the current page. This lets you turn
    # back to it easily. The book starts out without a bookmark.
    book3 = Book("The Name of the Wind", "Patrick Rothfuss", 662)
    assert (str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
            "662 pages, currently on page 1>")
    assert (book3.get_bookmarked_page() == None)
    book3.turn_page(9)
    book3.place_bookmark()  # does not return
    assert (book3.get_bookmarked_page() == 10)
    book3.turn_page(7)
    assert (book3.get_bookmarked_page() == 10)
    assert (book3.get_current_page() == 17)
    assert (str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
            "662 pages, currently on page 17, page 10 bookmarked>")
    book3.turn_to_bookmark()
    assert (book3.get_current_page() == 10)
    book3.remove_bookmark()
    assert (book3.get_bookmarked_page() == None)
    book3.turn_page(25)
    assert (book3.get_current_page() == 35)
    book3.turn_to_bookmark()  # if there's no bookmark, don't turn to a page
    assert (book3.get_current_page() == 35)
    assert (str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
            "662 pages, currently on page 35>")

    # Finally, you should be able to compare two books directly
    book5 = Book("A Game of Thrones", "George R.R. Martin", 807)
    book6 = Book("A Game of Thrones", "George R.R. Martin", 807)
    book7 = Book("A Natural History of Dragons", "Marie Brennan", 334)
    book8 = Book("A Game of Spoofs", "George R.R. Martin", 807)
    assert (book5 == book6)
    assert (book5 != book7)
    assert (book5 != book8)
    book5.turn_page(1)
    assert (book5 != book6)
    book5.turn_page(-1)
    assert (book5 == book6)
    book6.place_bookmark()
    assert (book5 != book6)
    print("Done!")

if __name__ == '__main__':
    test_book_class()
