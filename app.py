import json

# File to store library data
LIBRARY_FILE = "library.json"

def load_library():
    """Loads the library data from a file."""
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    """Saves the library data to a file."""
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    """Adds a new book to the library."""
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    year = input("Enter publication year: ").strip()
    genre = input("Enter genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    save_library(library)
    print("Book added successfully!\n")

def remove_book(library):
    """Removes a book from the library."""
    title = input("Enter the title of the book to remove: ").strip()
    
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            print("Book removed successfully!\n")
            return
    print("Book not found.\n")

def search_books(library):
    """Searches for books by title or author."""
    query = input("Enter title or author to search: ").strip().lower()
    matches = [book for book in library if query in book["title"].lower() or query in book["author"].lower()]
    
    if matches:
        print("\nSearch Results:")
        for book in matches:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {'Yes' if book['read'] else 'No'}")
    else:
        print("No matching books found.")
    print()

def display_books(library):
    """Displays all books in the library."""
    if not library:
        print("No books in the library.\n")
        return
    
    print("\nLibrary Collection:")
    for book in library:
        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {'Yes' if book['read'] else 'No'}")
    print()

def display_statistics(library):
    """Displays statistics about the library."""
    total_books = len(library)
    if total_books == 0:
        print("No books in the library.\n")
        return
    
    read_books = sum(1 for book in library if book['read'])
    read_percentage = (read_books / total_books) * 100
    
    print(f"\nTotal Books: {total_books}")
    print(f"Books Read: {read_books} ({read_percentage:.2f}%)\n")

def main():
    """Main function to run the Personal Library Manager."""
    library = load_library()
    
    while True:
        print("Personal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    main()
