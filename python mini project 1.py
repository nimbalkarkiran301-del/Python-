shopping_list = []

while True:
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Display Items")
    print("3. Search Item")
    print("4. Remove Item")
    print("5. Count Items")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Add Item
    if choice == 1:
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(item, "added successfully.")

    # Display Items
    elif choice == 2:
        if len(shopping_list) == 0:
            print("Shopping list is empty.")
        else:
            print("Shopping List:")
            for i in shopping_list:
                print("-", i)

    # Search Item
    elif choice == 3:
        item = input("Enter item to search: ")
        if item in shopping_list:
            print(item, "is found in the list.")
        else:
            print(item, "is not found.")

    # Remove Item
    elif choice == 4:
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed successfully.")
        else:
            print(item, "not found in the list.")

    # Count Items
    elif choice == 5:
        print("Total items in shopping list:", len(shopping_list))

    # Exit
    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")