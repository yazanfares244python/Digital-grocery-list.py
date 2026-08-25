# Important modules
from pathlib import Path
import json
# Unimportant module
from time import sleep
# Creating the class that is responsible for the critical points about the grocery list(Adding, Viewing, Deleting, Editing)
class DigitalGroceryList:
    # Initializing each variable thats gonna be used in this class
    def __init__(self):
        self.item = None
        self.amount = 0
        self.price = 0.0
        self.grocery_list = []
        self.total_price = 0.0
        self.edit_option = None
        self.amount_of_items = 0
        self.budget = 0.0
        # This is from the DigitalGroceryListData class its in the DigitalGroceryList class to prevent overwriting inherited variables which therefore leads to AttributeError's
        self.option = None
    # Creating the function that adds item information to the grocery list
    def add_item_info(self):
        # Asking for the item while checking if its valid or found
        while True:
            self.item = input("Enter the item that you want to add to the grocery list ->: ").capitalize()
            if not self.item:
                print("Enter a valid item")
            elif any(self.item == groceries["Item"] for groceries in self.grocery_list):
                print("\nItem already found")
                break
            else:
                # Asking for the amount while checking if its valid or not
                while True:
                    try:
                        self.amount = int(input(f"Enter the amount of {self.item}s you got ->: "))
                        if self.amount <= 0:
                            print("Enter an amount that is bigger than 0")
                        else:
                            break
                    except ValueError:
                        print("Invalid amount")
                # Asking for the price of one item while checking if its valid or not
                while True:
                    try:
                        self.price = float(input(f"Enter the price of one {self.item} ->: "))
                        if self.price <= 0.0:
                            print("Enter a price that is bigger than 0")
                        else:
                            break
                    except ValueError:
                        print("Invalid price")
                self.grocery_list.append({"Item": self.item, "Amount": self.amount, "Price": self.amount*self.price, "Bought": False})
                print(f"\n{self.amount} {self.item}(s) has been successfully added to the grocery list")
                break
    # Creating the function that displays the grocery list
    def display_grocery_list(self):
        # Check if grocery list data exists
        if not self.grocery_list:
            print("\nNo data found to proceed")
        else:
            print("\nGrocery List: ")
            # Looping through each item information
            for item_info in self.grocery_list:
                print() # <- This is to seperate each item information for clearer structure
                for item_info_key, item_info_value in item_info.items():
                    if item_info_key == "Price":
                        print(f"{item_info_key} -> {item_info_value:.2f}")
                    elif item_info_key == "Bought":
                        if item_info_value:
                            print(f"{item_info_key} -> ✅")
                        elif not item_info_value:
                            print(f"{item_info_key} -> ❌")
                    else:
                        print(f"{item_info_key} -> {item_info_value}")
    # Creating the function that deletes an item alongside its information
    def delete_item(self):
        # Asking for the item while checking if its valid or found
        while True:
            self.item = input("Enter the item that you want to delete from the grocery list ->: ").capitalize()
            if not self.item:
                print("Enter a valid item")
            elif all(self.item != groceries["Item"] for groceries in self.grocery_list):
                print("\nNo such item found")
                break
            else:
                # Looping through each item information
                for item_info in self.grocery_list:
                    if self.item == item_info["Item"]:
                        self.grocery_list.remove(item_info)
                        print(f"\nThe item {self.item} has been successfully deleted from the grocery list")
                        break
                    else:
                        continue
                break
    # Creating the function that resets the grocery list
    def reset_grocery_list(self):
        # Check if grocery list data exists
        if not self.grocery_list:
            print("\nNo data found to proceed")
        else:
            self.grocery_list.clear()
            print("\nThe grocery list has been successfully cleared")
    # Creating the function that edits an item's information(Name/Amount/Price)
    def edit_item_info(self):
        # Asking for the item while checking if its valid or found
        while True:
            self.item = input("Enter the item that you want to edit ->: ").capitalize()
            if not self.item:
                print("Enter a valid item")
            elif all(self.item != item_info["Item"] for item_info in self.grocery_list):
                print("\nNo such item found")
                break
            else:
                # Asking the user on what they would like to edit
                self.edit_option = input(f"Enter the attribute that you would like to change about {self.item}(Enter N for Name, A for Amount, P for Price) ->: ").upper().strip()
                if self.edit_option == 'N':
                    # Looping through each item information
                    for item_info in self.grocery_list:
                        if item_info["Item"] == self.item:
                            # Asking for the item while checking if its valid or found
                            while True:
                                self.item = input("Enter the item in the way you want to edit it ->: ").capitalize()
                                if not self.item:
                                    print("Enter a valid name")
                                elif any(self.item == item_info["Item"] for item_info in self.grocery_list):
                                    print("\nItem already found(Delete the old item you entered)")
                                    break
                                else:
                                    item_info["Item"] = self.item
                                    print(f"\nThe item has been successfully edited to {self.item}")
                                    break
                            break
                        else:
                            continue
                elif self.edit_option == "A":
                    # Looping through each item information
                    for item_info in self.grocery_list:
                        if item_info["Item"] == self.item:
                            # Setting the full price into the singular price to calculate the full price after the new amount
                            item_info["Price"] /= item_info["Amount"]
                            # Asking for the new amount while checking if its valid or not
                            while True:
                                try:
                                    self.amount = int(input(f"Enter the new amount of {self.item}s you got ->: "))
                                    if self.amount <= 0:
                                        print("Enter an amount that is bigger than 0")
                                    else:
                                        break
                                except ValueError:
                                    print("Invalid amount")
                            item_info["Amount"] = self.amount
                            item_info["Price"] *= self.amount
                            print(f"\nThe {self.item}'s amount has been successfully edited to {self.amount}")
                            break
                        else:
                            continue
                elif self.edit_option == "P":
                    # Looping through each item information
                    for item_info in self.grocery_list:
                        if item_info["Item"] == self.item:
                            # Asking for the new singular price
                            while True:
                                try:
                                    self.price = float(input(f'Enter the new price of one {self.item} ->: '))
                                    if self.price <= 0.0:
                                        print("Enter a price that is bigger than 0")
                                    else:
                                        break
                                except ValueError:
                                    print("Invalid price")
                            item_info["Price"] = item_info["Amount"]*self.price
                            print(f"\nThe {self.item}'s total price has been successfully edited to {item_info['Price']:.2f}")
                            break
                        else:
                            continue
                else:
                    print("\nInvalid choice")
                break
    # Creating the function that displays the total price
    def display_total_price(self):
        self.total_price = sum(groceries["Price"] for groceries in self.grocery_list)
        print("\nTotal Price: \n")
        # Check if the total price is bigger than 0
        if self.total_price == 0.0:
            print("No data found")
        else:
            # Looping through each item information
            for item_info in self.grocery_list:
                print(f"{item_info['Item']} -> {item_info['Price']:.2f}")
            print(" +                                ")
            print("__________________________________")
            print(f"        {self.total_price:.2f}")
    # Creating the function that displays the amount of items found
    def display_amount_of_items(self):
        self.amount_of_items = sum(groceries["Amount"] for groceries in self.grocery_list)
        print("\nAmount of items found: \n")
        # Check if the amount of items is bigger than 0
        if self.amount_of_items == 0:
            print("No data found")
        else:
            # Looping through each item information
            for item_info in self.grocery_list:
                print(f"{item_info['Item']} -> {item_info['Amount']}")
            print(" +                                 ")
            print("__________________________________")
            print(f"         {self.amount_of_items}")
    # Creating the function that marks an item as a green mark for bought
    def mark_item(self):
        # Asking for the item while checking if its valid or found
        while True:
            self.item = input("Enter the item that you would like to mark as bought ->: ").capitalize()
            if not self.item:
                print("Enter a valid item")
            elif all(self.item != groceries["Item"] for groceries in self.grocery_list):
                print("\nNo such item found")
                break
            else:
                # Looping through each item information
                for item_info in self.grocery_list:
                    if item_info["Item"] == self.item:
                        # Check if its already marked
                        if item_info["Bought"]:
                            print("\nThe item is already marked")
                            break
                        else:
                            item_info["Bought"] = True
                            print(f"\nThe item {self.item} has been successfully marked as bought")
                            break
                    else:
                        continue
                break
    # Creating the function that unmarks an item
    def unmark_item(self):
        # Asking for the item while checking if its valid or found
        while True:
            self.item = input("Enter the item that you would like to unmark ->: ").capitalize()
            if not self.item:
                print("Enter a valid item")
            elif all(self.item != groceries["Item"] for groceries in self.grocery_list):
                print("\nNo such item found")
                break
            else:
                # Looping through each item information
                for item_info in self.grocery_list:
                    if item_info["Item"] == self.item:
                        # Check if its marked or not
                        if not item_info["Bought"]:
                            print("\nThe item is already not marked")
                            break
                        else:
                            item_info["Bought"] = False
                            print(f"\nThe item {self.item} has successfully been unmarked as bought")
                            break
                    else:
                        continue
                break
    # Creating the function that searches an item and returns it's information
    def search_item_info(self):
        # Asking for the item while checking if its valid or found
        while True:
            self.item = input('Enter the item whose information you would like to search ->: ').capitalize()
            if not self.item:
                print("Enter a valid item")
            elif all(self.item != groceries["Item"] for groceries in self.grocery_list):
                print("\nNo such item found")
                break
            else:
                print(f"\nThe {self.item}'s information: \n")
                # Looping through each item information
                for item_info in self.grocery_list:
                    if item_info["Item"] == self.item:
                        # Looping through the item information's keys and values
                        for item_info_key, item_info_value in item_info.items():
                            if item_info_key == "Price":
                                print(f"{item_info_key} -> {item_info_value:.2f}")
                            elif item_info_key == "Bought":
                                if item_info_value:
                                    print(f"{item_info_key} -> ✅")
                                else:
                                    print(f"{item_info_key} -> ❌")
                            else:
                                print(f"{item_info_key} -> {item_info_value}")
                    else:
                        continue
                break
    # Creating the function that sets a budget and checks if the list is enough or not
    def set_and_check_budget(self):
        # Check if grocery list data exists
        if not self.grocery_list:
            print("\nNo data found to proceed")
        else:
            # Setting the total price to calculate if its enough or not
            self.total_price = sum(groceries['Price'] for groceries in self.grocery_list)
            # Asking for the budget while checking if its valid or not
            while True:
                try:
                    self.budget = float(input("Enter your budget ->: "))
                    if self.budget <= 0.0:
                        print('Enter a valid budget that is bigger than zero')
                    else:
                        if self.budget > self.total_price:
                            print(f"\nYour budget is enough(change left -> {self.budget - self.total_price:.2f})")
                        elif self.budget == self.total_price:
                            print("\nYour budget is enough but you won't have any change left")
                        else:
                            print("\nYour budget is not enough you can enter a new budget")
                            # Looping through each item information 
                            for item_info in self.grocery_list:
                                # Checking if removing a specific item will make the budget appropriate
                                if (self.total_price - item_info["Price"]) <= self.budget:
                                    print(f"or you can remove {item_info['Item']} from the grocery list which will make the total price into {self.total_price - item_info['Price']:.2f} which will be enough for your budget")
                                else:
                                    continue
                            break
                        break
                except ValueError:
                    print("Invalid budget")
# Creating the class that is responsible for the CLI commands and inheriting most of the variables from the DigitalGroceryList class to avoid AttributeErrors
class DigitalGroceryListCLI(DigitalGroceryList):
    # Creating the function that displays the menu and asks the user for their option
    def display_menu(self):
        print("--- Digital Grocery List ---")
        DigitalGroceryListData.read_data(self)
        while True:
            print("\n1. Add an item")
            print("2. View grocery list")
            print("3. Delete an item")
            print("4. Reset grocery list")
            print("5. Edit an item's information(Name/Amount/Price)")
            print("6. View total price")
            print("7. View the amount of items in the list")
            print("8. Mark an item as bought")
            print("9. Unmark an item")
            print("10. Search for an item with its information")
            print("11. Set a budget and check if its enough or not")
            print("12. Exit")
            self.option = input("Enter your option(1-12) ->: ")
            if self.option == '1':
                DigitalGroceryList.add_item_info(self)
            elif self.option == '2':
                DigitalGroceryList.display_grocery_list(self)
            elif self.option == '3':
                DigitalGroceryList.delete_item(self)
            elif self.option == '4':
                DigitalGroceryList.reset_grocery_list(self)
            elif self.option == '5':
                DigitalGroceryList.edit_item_info(self)
            elif self.option == '6':
                DigitalGroceryList.display_total_price(self)
            elif self.option == '7':
                DigitalGroceryList.display_amount_of_items(self)
            elif self.option == '8':
                DigitalGroceryList.mark_item(self)
            elif self.option == '9':
                DigitalGroceryList.unmark_item(self)
            elif self.option == '10':
                DigitalGroceryList.search_item_info(self)
            elif self.option == '11':
                DigitalGroceryList.set_and_check_budget(self)
            elif self.option == '12':
                print("Ok wait a moment...")
                sleep(1.5)
                print("Saving data...")
                DigitalGroceryListData.write_data(self)
                sleep(2)
                print("Exiting...")
                sleep(1.5)
                break
            else:
                print("\nInvalid option")
# Creating the class that is responsible for the data parsing
class DigitalGroceryListData:
    # Initializing each variable thats gonna be used in this class
    def __init__(self):
        self.grocery_list = []
    # Creating the function that reads the data from the file to the program
    def read_data(self):
        # Check if the file exists
        if Path("grocery_list.json").is_file():
            with open("grocery_list.json", "r") as f:
                self.grocery_list = json.load(f)
    # Creating the function that writes the data from the program to the file
    def write_data(self):
        with open("grocery_list.json", "w") as f:
            json.dump(self.grocery_list, f)
grocery_list_app = DigitalGroceryListCLI()
grocery_list_app.display_menu()
