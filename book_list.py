#userinterface milestone 1

import json

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
    # Serializing json
    json_object = json.dumps(book_list, indent=4)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
    print(f"Book '{title}' added")



def view_book():

    with open('sample.json', 'r') as file:
            # Reading from json file
        try:
            json_object = json.load(file)
            # print(json_object) instead of this, use below
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

            book_to_rate = int(input("Please select the number of the book to rate: ")) - 1
            if book_to_rate < 0 or book_to_rate >= len(json_object):
                print("Invalid selection. Please try again.")
                return

            rate_number = input(f"Enter your rating for '{json_object[book_to_rate]['Title']}' (1-5): ")
            if not rate_number.isdigit() or int(rate_number) < 1 or int(rate_number) > 5:
                print("Invalid rating. Please enter a number between 1 and 5.")
                return

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
    user_ratings = [rate for rate in rate_list if rate["User"] == user_name]
    if not user_ratings:
        print("No ratings found for this user.")
        return

    highest_rated_book = max(user_ratings, key=lambda x: x['Rating'])
    print(f"Recommendations:\nTitle: {highest_rated_book['Book']}, Rating: {highest_rated_book['Rating']}")







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
            print("search book")
        elif user_input == "6":
            break
        else:
            print("Invalid choice. Please try again.")





main()
