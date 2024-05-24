import json


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.books = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, title, book):
        node = self.root
        for char in title:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.books.append(book)

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._collect_all_books(node)

    def _collect_all_books(self, node):
        books = []
        if node.is_end_of_word:
            books.extend(node.books)
        for child in node.children.values():
            books.extend(self._collect_all_books(child))
        return books

trie = Trie()

def main_menu():
    print("Options:")
    print("1. Add Book")
    print("2. View Books")
    print("3. Rate Book")
    print("4. Get Recommendations")
    print("5. Search Books")
    print("6. Exit")


book_list = []
rate_list = []

def add_book():
    title = input ("Enter book title:")
    author = input("Enter book author:")
    genre = input("Enter book genre:")

    book_dict= {
        "Title": title,
        "Author": author,
        "Genre": genre,
    }

    book_list.append(book_dict)
    trie.insert(title.lower(), book_dict)

    json_object = json.dumps(book_list, indent=4)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
    print(f"Book '{title}' added")



def view_book():

    with open('sample.json', 'r') as file:

        try:
            json_object = json.load(file)
            for index, book in enumerate(json_object, start=1):
                print(f"{index}. Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}")
        except json.JSONDecodeError:
            print("No books available")


def rate_book():
    user_name = input("Enter your username: ")
    try:
        with open('sample.json', 'r') as file:
            json_object = json.load(file)
            for index, book in enumerate(json_object, start=1):
                print(f"{index}. Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}")

            while True:
                book_to_rate = int(input("Please select the number of the book to rate: ")) - 1
                if book_to_rate < 0 or book_to_rate >= len(json_object):
                    print("Invalid selection. Please try again.")
                else:
                    break

            while True:
                rate_number = input(f"Enter your rating for '{json_object[book_to_rate]['Title']}' (1-5): ")
                if not rate_number.isdigit() or int(rate_number) < 1 or int(rate_number) > 5:
                    print("Invalid rating. Please enter a number between 1 and 5.")
                else:
                    break

            rate_number = int(rate_number)
            rate_dict = {
                "User": user_name,
                "Book": json_object[book_to_rate]['Title'],
                "Rating": rate_number
            }
            rate_list.append(rate_dict)
            print(f"Rating '{rate_number}' added for '{json_object[book_to_rate]['Title']}' by user '{user_name}'.")

    except (FileNotFoundError, json.JSONDecodeError):
        print("No books available to rate. Please add one first.")




def get_rec():
    user_name = input("Enter your username: ")
    user_ratings = []
    for rate in rate_list:
        if rate["User"] == user_name:
            user_ratings.append(rate)
    if not user_ratings:
        print("No ratings found for this user.")
        return

    highest_rated_book = max(user_ratings, key=lambda x: x['Rating'])
    print(f"Recommendations:\nTitle: {highest_rated_book['Book']}, Rating: {highest_rated_book['Rating']}")



def search_books():
    prefix = input("Enter book title prefix: ").lower()
    results = trie.search(prefix)
    if results:
        print("Search Results:")
        for book in results:
            print(f"Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}")
    else:
        print("No books found with that prefix.")



def main():
    while True:

        main_menu()
        user_input = input("Choose an option: ")
        if user_input == "1":
            add_book()
        elif user_input == "2":
            view_book()
        elif user_input == "3":
            rate_book()
        elif user_input == "4":
            get_rec()
        elif user_input == "5":
            search_books()
        elif user_input == "6":
            break
        else:
            print("Invalid choice. Please try again.")





main()
