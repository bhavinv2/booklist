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



# def view_book():
#     try:
#         with open('sample.json', 'r') as file:
#             # Reading from json file
#             json_object = json.load(file)
#         print(json_object)
#     except FileNotFoundError:
#         print("No books")

def view_book():

    with open('sample.json', 'r') as file:
            # Reading from json file
        try:
            json_object = json.load(file)
        except json.JSONDecodeError:
            json_object = []

    if not json_object:
        print("No books available.")
    else:
        for index, book in enumerate(json_object, start=1):
            print(f"{index}. Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}")






def main():
    while True:

        main_menu()
        user_input = input("Choose an option: ")
        if user_input == "1":
            add_book()
        elif user_input == "2":
            view_book()
        elif user_input == "3":
            print("rate book")
        elif user_input == "4":
            print("rec book")
        elif user_input == "5":
            print("search book")
        elif user_input == "6":
            break
        else:
            print("Invalid choice. Please try again.")





main()
