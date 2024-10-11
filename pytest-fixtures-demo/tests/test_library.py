from app import Library

def test_add_book():
    library = Library()

    library.add_book("The Gone with the wind", "M. Mitchell")
    assert library.books == {"author":"M. Mitchell", "title": "The Gone with the wind"}
