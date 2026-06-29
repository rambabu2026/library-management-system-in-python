# I build a project library managment system 

books = []

while True:
    print("========== Library Management System ==========")
    print(" 1. Add Book\n " \
    "2. View Books\n " \
    "3. Search Book\n " \
    "4. Borrow Book\n " \
    "5. Return Book\n " \
    "6. Delete Book\n " \
    "7. Exit\n")
    
    choice = int(input("Enter your choice (1,2,3,4,5,6,7) : "))
    if choice == 1:
        book_id = input("Enter book id : ")
        book_name = input("Enter book name : ")
        book_author = input("Enter author name : ")
        book_aval = True

        book = {
        "id" : book_id,
        "name" : book_name,
        "author" : book_author,
        "available" : book_aval
        }

        books.append(book)
        print(books)
        print("Record added successfull !")

    elif choice == 2:
        if not books:
            print("Not books available!")
        else:
            for book in books:
                print(f"\nBook Id: {book['id']}")
                print(f"Book name: {book['name']}")
                print(f"Book author: {book['author']}")
                print(f"Book availabel: {book['available']}\n")
    
    elif choice == 3:
        search_book_name = input("Enter book name : ")
        found = False
        for book in books:
            if book["name"].lower() == search_book_name.lower():
                found = True
                print(f"\nBook Id: {book['id']}")
                print(f"Book name: {book['name']}")
                print(f"Book author: {book['author']}")
                print(f"Book availabel: {book['available']}")
                break
        if not found:
                print("Book Not Found!")
    elif choice == 4:
        borrow_book = input("Enter book name : ")
        found = False
        for book in books:
            if book["name"].lower() == borrow_book.lower():
                found = True
                if book["available"]:
                    book["available"] = False
                    print("Book Borrowed Successfully!")
                else:
                    print("Book is already borrowed !")
                break
        if not found:
            print("Book not found !")
    elif choice == 5:
        return_book = input("Enter return book : ")
        found = False
        for book in books:
            if book["name"].lower() == return_book.lower():
                found = True
                if not book ["available"]:
                    # book["False"]:
                    book["available"] = True
                    print("Book Returned Successfully !")
                else:
                    print("Book was not borrowed !")
                break
        if not found:
            print("Book not found !")
    elif choice == 6:
        delete_book = input("Enter book name : ")
        found = False
        for book in books:
            if book["name"].lower() == delete_book.lower():
                found = True
                books.remove(book)
                print("Book deleted successfully !")
                break
        if not found:
            print("Book not found!")
    elif choice == 7:
        print("Thank You!")
        break