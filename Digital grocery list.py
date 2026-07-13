# Important modules
import os
import json
# Unimportant module
from time import sleep
# The grocery list
grocery_list = []
# Saving the grocery data back to the list
if os.path.exists("grocery_list.json"):
    with open("grocery_list.json", "r") as f:
        grocery_list = json.load(f)
# Creating the function that asks the user for an input to add to the list
def ask_input():
    return input("Enter the item that you wanna add to the grocery list ->: ").capitalize().strip()
# Creating the main function
def digitial_grocery_list():
    print("--- Digital Grocery List ---")
    while True:
        print("\n1. Add an item")
        print("2. View grocery list")
        print("3. Delete from list")
        print("4. Clear list")
        print("5. Exit")
        option = input("Enter your choice(1-5) ->: ")
        if option == '1':
            add_item = ask_input()
            while True:
                if not add_item:
                    print("Enter a valid item")
                    add_item = ask_input()
                elif add_item in grocery_list:
                    print("Item already found")
                    break
                else:
                    grocery_list.append(add_item)
                    print(f"\nThe item {add_item} has been successfully added to the grocery list")
                    break
        elif option == '2':
            # Check if groecery list data exists
            if not grocery_list:
                print("\nNo data found to proceed")
            else:
                print("List: \n")
                for item in grocery_list:
                    print(item)
        elif option == '3':
            # Check if groecery list data exists
            if not grocery_list:
                print("\nNo data found to proceed")
            else:
                delete_item = ask_input()
                while True:
                    if not delete_item:
                        print("Enter a valid item")
                        delete_item = ask_input()
                    elif delete_item not in grocery_list:
                        print("No such item found")
                        break
                    else:
                        grocery_list.remove(delete_item)
                        print(f"\nThe item {delete_item} has been successfully removed from the grocery list")
                        break
        elif option == '4':
            # Check if groecery list data exists
            if not grocery_list:
                print("\nNo data found to proceed")
            else:
                grocery_list.clear()
                print("\nThe grocery list has been successfully cleared")
        elif option == '5':
            print("Ok wait a moment...")
            sleep(1.5)
            print("Saving data...")
            with open("grocery_list.json", "w") as f:
                json.dump(grocery_list, f)
            sleep(2)
            print("Exiting...")
            sleep(1.5)
            break
        else:
            print("Invalid choice")
if __name__ == '__main__':
    digitial_grocery_list()

