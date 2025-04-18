import json
import os

BOOKS_FILE = "books.json"

# Load books from file
def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save books to file
def save_books(books):
    with open(BOOKS_FILE, 'w') as file:
        json.dump(books, file, indent=4)

# Add a new book
def add_book(books):
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    
    try:
        year = int(input("Enter publication year: "))
    except ValueError:
        print("Invalid year! Please enter a number.")
        return

    genre = input("Enter genre: ").strip()
    read_status = input("Have you read it? (Read / Not Read): ").strip().title()
    
    if read_status not in ["Read", "Not Read"]:
        print("Invalid read status. Must be 'Read' or 'Not Read'.")
        return

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read_status": read_status
    }
    books.append(book)
    save_books(books)
    print(f"✅ '{title}' has been added.")

# Remove a book by title
def remove_book(books):
    title = input("Enter the title of the book to remove: ").strip()
    found = False
    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            save_books(books)
            print(f"🗑️ '{title}' has been removed.")
            found = True
            break
    if not found:
        print("❌ Book not found.")

# Search books
def search_books(books):
    keyword = input("Enter title or author to search: ").strip().lower()
    results = [book for book in books if keyword in book["title"].lower() or keyword in book["author"].lower()]
    
    if results:
        print(f"🔍 Found {len(results)} result(s):")
        for book in results:
            display_book(book)
    else:
        print("❌ No matching books found.")

# Display a single book
def display_book(book):
    print(f"\n📖 Title: {book['title']}")
    print(f"✍️ Author: {book['author']}")
    print(f"📅 Year: {book['year']}")
    print(f"🏷️ Genre: {book['genre']}")
    print(f"📘 Status: {book['read_status']}")

# Display all books
def display_all_books(books):
    if not books:
        print("📚 Your library is empty.")
        return
    print(f"\n📚 You have {len(books)} book(s) in your library:\n")
    for book in books:
        display_book(book)

# View statistics
def view_statistics(books):
    total = len(books)
    if total == 0:
        print("📊 No statistics to show. Library is empty.")
        return
    read_count = sum(1 for book in books if book["read_status"] == "Read")
    print(f"\n📊 Total books: {total}")
    print(f"✅ Books read: {read_count} ({(read_count / total) * 100:.2f}%)")
    print(f"📖 Books not read: {total - read_count}")

# Main menu
def main():
    books = load_books()

    while True:
        print("\n===== Personal Library Manager =====")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search Books")
        print("4. Display All Books")
        print("5. View Statistics")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            remove_book(books)
        elif choice == "3":
            search_books(books)
        elif choice == "4":
            display_all_books(books)
        elif choice == "5":
            view_statistics(books)
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
