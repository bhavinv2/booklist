Book Recommendation System

Overview

The Book Recommendation System is a console-based application designed to help users manage and rate books efficiently. It supports adding books, viewing books, rating books, getting recommendations, and searching for books by title. All book data and user ratings are saved to a file for persistence between sessions.

Features

Add Books: Add new books with title, author, and genre.
View Books: View a list of all available books.
Rate Books: Rate books by specifying the book number.
Get Recommendations: Receive book recommendations based on user ratings.
Search Books: Search for books by title prefix.
Persistent Storage: Books and ratings are saved to a JSON file to retain data between sessions.
Components

Trie
A Trie data structure for managing and searching book titles efficiently.

TrieNode Class: Represents a single node in the Trie.
Trie Class: Manages the Trie with methods to insert and search for book titles.
BookManager
The main class that integrates the Trie to manage books and user ratings.

add_book: Adds a book with title, author, and genre.
view_books: Displays all books.
rate_book: Rates a specified book.
get_rec: Provides book recommendations based on ratings.
search_books: Searches for books by title prefix.
save_books: Saves books and ratings to a JSON file.
load_books: Loads books and ratings from a JSON file.
User Interface
A function to manage user inputs and interactions with the BookManager.

How to Use

Run the Program
Execute the script in a Python environment.

Follow Prompts
The application will display a menu with options.


Sample interaction
Options:
1. Add Book
2. View Books
3. Rate Book
4. Get Recommendations
5. Search Books
6. Exit
Choose an option: 1

Enter book title: Harry Potter
Enter book author: J.K. Rowling
Enter book genre: Fantasy
Book 'Harry Potter' added successfully.

Requirements

Python 3.x
json module (standard library)
File Structure

book_recommendation_system.py: Main script file containing all classes and functions.
sample.json: File where books and ratings are stored.
Notes

Make sure to run the script in a directory where sample.json can be created and accessed.
Ensure Python 3.x is installed on your system.
