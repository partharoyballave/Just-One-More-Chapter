#   Mar 1, 2023                         Just One More Chapter                Roy Ballave, Partha
#
# The program simulates an artificial bookstore where it's database is manipulable. Users can search for
# books by author, view all available books, add a new author and book to the store, and
# remove an author and their book(s) from the store.
#


# User Interface
def show_options():
    print(" -----------------------------------------------------------------------")
    print("                          Just One More Chapter 📖")
    print("                                 Options:")
    print("   (1):  Find a book by author")
    print("   (2):  View all the books")
    print("   (3):  Add a new author and book")
    print("   (4):  Remove an author and their book(s)")

    print(" -----------------------------------------------------------------------\n")

    option = input("Please choose an option: ")

    return option

# List Checking
def item_in_list(x, list1):
    item_in_list = False

    for i in list1:
        if i == x:
            item_in_list = True

    return item_in_list

# Finds an author and their books in lists + error statement
def find_authors_books(authors_name, authors_list, list_of_books):
    in_list = False
    for author in authors_list:
        if author == authors_name:
            in_list = True

    if in_list == True:
        print(f"\n{authors_name} wrote the following books:\n")

        for i in range(len(authors)):
            if authors[i] == authors_name:
                print(f"{list_of_books[i]}")

    else:
        print(f"{authors_name} is not an author of a book in the store. Please try again.")
    return in_list
# Recieves a new book and author from the user and adds it to the list.
def add_author(authors_list, books_list):
    authors_name = input("Please enter the name of the author: ")
    books_name = input("Please enter the name of the book: ")

    authors_list.append(authors_name)
    books_list.append(books_name)
    print(f"{authors_name}'s book '{books_name}' has been added to Just One More Chapter.\n")

    return authors_list, books_list

# Receives an author already in the list and removes it, + error statement
def remove_author(authors_list, books_list):
    while True:
        author_to_remove = input("Please enter the author to remove: ")
        author_In_List = item_in_list(author_to_remove, authors_list)
        if author_In_List == False:
            print("This author does not have a book in Just One More Chapter, try again.\n")
            continue
        break

    while True:
        book_to_remove = input("Please enter the book to remove: ")
        if item_in_list(book_to_remove, books_list) == False:
            print("The book is not a valid book, try again.\n")
            continue
        break

    new_authors = []
    new_books = []

    for i in books_list:
        if i != book_to_remove:
            new_authors.append(i)
            new_books.append(i)

    print(f"The book has been removed from the store.\n")

    return new_authors, new_books


# List of authors and books in the store
authors = ["Jhumpa Lahiri", "Arundhati Roy", "Fatima Farheen Mirza", "Aravind Adiga", "Mohsin Hamid",
           "Mindy Kaling", "Vikram Seth", "Rohinton Mistry", "Mohsin Hamid"]

books = ["Interpreter of Maladies", "The God of Small Things", "A Place for Us", "The White Tiger",
         "How to Get Filthy Rich in Rising Asia", "Is Everyone Hanging Out Without Me?", "A Suitable Boy",
         "A Fine Balance", "The Reluctant Fundamentalist"]


# MAIN PROGRAM
program_On_Or_Off = True

while program_On_Or_Off == True:

    book_Options = show_options()
# Option 1
    if book_Options == "1":
        print()
        authors_Name = input("Enter the author's name: ")
        author_In_List = find_authors_books(authors_Name, authors, books)
        continue
# Option 2
    if book_Options == "2":

        for i in range(len(authors)):
            print(f"{books[i]}, by {authors[i]}")
        print()
# Option 3
    if book_Options == "3":
        authors, books = add_author(authors, books)
# Option 4
    if book_Options == "4":
        authors, books = remove_author(authors, books)

# Hard Stop Feature
    continue_The_Program = input("Would you like to keep going and change something? (Y/n)").lower()
    if continue_The_Program == "n":
        program_On_Or_Off = False
        print("Thank you for shopping at Just One More Chapter!")