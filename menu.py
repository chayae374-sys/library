def print_menu():
    return  """ 
    ================================
       LIBRARY MANAGEMENT
================================

1. Display all books
2. Search book by name
3. Add new book
4. Borrow a book
5. Return a book
6. Display available books
7. Display books by author
8. Exit

Choose an option:
"""

    
def choise():
    user = False
    while not user:
        try:
            user_choise = int(input("enter your choise! "))
            if 0 < user_choise < 9:
                user = True
            else: 
                print("just between 1-8")
        except ValueError:
            print("just a number")
    return user_choise    
    

