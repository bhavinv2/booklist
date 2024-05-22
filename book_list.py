#userinterface milestone 1

def main_menu():
    print("Options:")
    print("1. Add Book")
    print("2. View Books")
    print("3. Rate Book")
    print("4. Get Recommendations")
    print("5. Search Books")
    print("6. Exit")


def main():
    while True:
        main_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            #add_book()
        elif choice == "2":
            #view_books()
        elif choice == "3":
            #rate_book()
        elif choice == "4":
            #get_recommendations()
        elif choice == "5":
            #search_books()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
