
#שאלה 1
def display_all_books(books):
    for book in books:
        print( book["name"])


#שאלה 2
def search_book_by_name(books,name):
    for book in books:
        if book["name"][:len(name)].lower() == name.lower():
            print( book)
        
#שאלה 3           
def add_new_book(books, name, author, year):
    new_book =  { "id":get_next_book_id(books),        "name":name,        "author": author,        "year": year,        "available": True    }
    books.append(new_book)
    return True
    
#שאלה 4
def borrow_a_book(books,book_id):
     for book in books:
        if book_id== book["id"] and book["available"] == True:
            book["available"] == False
            print("The loan was successful")
            return True
        else:
            print("not found")
            return False
        
#שאלה 5           
def beturn_a_book(books,book_id):
    for book in books:
        if book_id == book["id"] and book["available"] == False:
            book["available"] == True
            print("The return was successful")
            return True
    print("not found")
    return False
    
#שאלה 6
def display_available_books(books):
    for book in books:
        if book["available"] == True:
            print(book)

def display_books_by_author(books, author):
    found  =False
    for book in books:
        if book["author"] == author.upper():
            found = True
            print(book)
            return True
        if not found:
            print("invaild author")
            return False
    

def get_next_book_id(books):
    return books[-1]["id"] + 1

            
            