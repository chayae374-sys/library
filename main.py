import working as w
from menu import print_menu,choise
from data import books

def main():
    user_choise = None
    while user_choise != 8:
        user_choise = choise()
        if user_choise == 1:
            w.display_all_books(books)
        elif user_choise == 2:
            name = input("what is the number of the book?")
            w.search_book_by_name(books,name)
        elif user_choise == 3:
            name = input("which name do you want to add?")
            auther = input("what is the author of the book?")
            year = input("what is the year?")
            w.add_new_book(books, name, author, year)
        elif user_choise == 4:
            id_book = None
            try:
                book_id = int(input("enter id of the book!"))
                w.borrow_a_book(books,book_id)
            except ValueError:
                print("the id must be a number")
        elif user_choise == 5:
            id_book = None
            try:
                book_id = int(input("enter id of the book!"))
                w.beturn_a_book(books,book_id)
            except ValueError:
                print("the id must be a number")
        elif user_choise == 6:
            w.display_available_books(books)
        elif user_choise == 7:
            author = input("what is the name of the author?")
            w.display_books_by_author(books, author)
            
if __name__ == "__main__":
    main()
        
            