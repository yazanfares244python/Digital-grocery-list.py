# Important modules
from pathlib import Path
import json
# Unimportant modules
from time import sleep
# Creating the class that is responsible for the main critical points about the digital grocery list(adding, viewing, deleting, marking, etc.)
class DigitalGroceryList:
    # Initializing each variable thats gonna be used in this class
    def __init__(self):
        self.item = None
        self.category = None
        self.amount = 0
        self.price = 0.0
        self.grocery_list = []
        self.budget = 0.0
        self.total_price = 0.0
        self.amount_of_items = 0
        # This variable is for the DigitalGroceryListCLI class 
        self.option = None
    # Creating the function that adds a new item to the grocery list
    def add_new_item(self):
        # Asking for the item while checking if its valid or not
        while True:
            self.item = input("Enter the item that you would like to add into the grocery list ->: ").capitalize()
            if not self.item:
                print("Enter a valid item")
            elif any(self.item == item_info["Item"] for item_info in self.grocery_list):
                print("\nItem already found")
                break
            else:
                # Asking for the category while checking if its valid or not
                while True:
                    self.category = input(f"Enter the category of {self.item}(Fruits, Snacks, etc.) ->: ").capitalize()
                    if not self.category:
                        print("Enter a valid category")
                    else:
                        break
                # Asking for the singular price while checking if its valid or not
                while True:
                    try:
                        self.price = float(input(f"Enter the price of one {self.item} ->: "))
                        if self.price <= 0:
                            print("Enter a valid price that is bigger than 0")
                        else:
                            break
                    except ValueError:
                        print("Invalid price")
                # Asking for the amount while checking if its valid or not
                while True:
                    try:
                        self.amount = int(input(f'Enter the amount of {self.item}s you got ->: '))
                        if self.amount <= 0:
                            print("Enter a valid amount that is bigger than 0")
                        else:
                            break
                    except ValueError:
                        print("Invalid amount")
                self.grocery_list.append({"Item": self.item, "Amount": self.amount, "Price": self.amount*self.price, "Category": self.category, "Bought": False})
                print(f'\n{self.amount} {self.item}(s) has been added into the grocery list')
                break
    # Creating the function that displays the items 
    def display_items(self):
        print("\nGrocery List: ")
        # Check if grocery list data exists
        if not self.grocery_list:
            print("\nNo data found to proceed")
        else:
            # Looping through each item information
            for item_info in self.grocery_list:
                print() # <- this is for clearer sturcture to seperate each item information one by one
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
    # Creating the function that deletes an item from the grocery list
    def delete_item(self):
        # Asking for the item while checking if its valid or found
        while True:
            self.item = input("Enter the item that you would like to delete ->: ").capitalize()
            if not self.item:
                print("Enter a valid item")
            elif all(self.item != item_info["Item"] for item_info in self.grocery_list):
                print("\nNo such item found")
                break
            else:
                # Looping through each item information
                for item_info in self.grocery_list:
                    if item_info["Item"] == self.item:
                        self.grocery_list.remove(item_info)
                        print(f"\nThe item {self.item} has been deleted from the grocery list")
                        break
                    else:
                        continue
                break
    # Creating the function that clears the grocery list
    def clear_grocery_list(self):
        # Check if grocery list data exists
        if not self.grocery_list:
            print("\nNo data found to proceed")
        else:
            self.grocery_list.clear()
            print("\nThe grocery list has been cleared")
    # Creating the function that edits an item's attribute(Name, Price, Amount, Category)
    def edit_item_attribute(self):
        # Asking for the item while checking if its valid or found
        while True:
            self.item = input("Enter the item whose attribute you would like to change ->: ").capitalize()
            if not self.item:
                print("Enter a valid item")
            elif all(self.item != item_info["Item"] for item_info in self.grocery_list):
                print("\nNo such item found")
                break
            else:
                self.option = input("Enter the attribute of the item that you would like to change(Enter N for Name, A for Amount, P for Price, C for Category) ->: ").upper().strip()
                if self.option == 'N':
                    # Looping through each item information
                    for item_info in self.grocery_list:
                        if item_info["Item"] == self.item:
                            # Asking for the new version of the item while checking if its valid or found
                            self.item = input(f"Enter the new version of {self.item} ->: ").capitalize()
                            if not self.item:
                                print('Enter a valid item')
                            elif any(self.item == item_info["Item"] for item_info in self.grocery_list):
                                print("\nItem already found(Delete the old one)")
                                break
                            else:
                                item_info["Item"] = self.item
                                print(f"\nThe item has been edited into {self.item}")
                                break
                        else:
                            continue
                elif self.option == 'A':
                    # Looping through each item information
                    for item_info in self.grocery_list:
                        if item_info["Item"] == self.item:
                            # Reseting the total price of an item into the singular price to do the final calculation after the new amount
                            item_info["Price"] /= item_info["Amount"]
                            # Asking for the new amount while checking if its valid or not
                            while True:
                                try:
                                    self.amount = int(input(f"Enter the new amount of {self.item}(s) you got ->: "))
                                    if self.amount <= 0:
                                        print("Enter a valid amount that is bigger than 0")
                                    else:
                                        break
                                except ValueError:
                                    print("Invalid amount")
                            item_info["Amount"] = self.amount
                            item_info["Price"] *= item_info["Amount"]
                            print("\nThe item's amount has been edited alongside its price")
                            break
                        else:
                            continue
                elif self.option == 'P':
                    # Looping through each item information
                    for item_info in self.grocery_list:
                        if item_info["Item"] == self.item:
                            # Asking for the new singular price while checking if tis valid or not
                            while True:
                                try:
                                    self.price = float(input(f"Enter the new price of one {self.item} ->: "))
                                    if self.price < 0:
                                        print("Enter a valid price that is bigger than 0")
                                    else:
                                        break
                                except ValueError:
                                    print("Invalid price")
                            item_info["Price"] = self.price*item_info["Amount"]
                            print(f"\nThe price has been edited into {item_info['Price']}")
                            break
                        else:
                            continue
                elif self.option == "C":
                    # Looping through each item information
                    for item_info in self.grocery_list:
                        if item_info["Item"] == self.item:
                            while True:
                                self.category = input(f"Enter the new category of {self.item} ->: ").capitalize()
                                if not self.category:
                                    print("Enter a valid category")
                                else:
                                    break
                            item_info["Category"] = self.category
                            break
                        else:
                            continue
                else:
                    print("\nInvalid option")
                break
    # Creating the function that marks an item as done
    def mark_item(self):
        # Asking for the item while checking if its valid or found
        while True:
            self.item = input("Enter the item that you would like to mark as bought ->: ").capitalize()
            if not self.item:
                print("Enter a valid item")
            elif all(self.item != item_info["Item"] for item_info in self.grocery_list):
                print("\nNo such item found")
                break
            else:
                # Looping through each item information
                for item_info in self.grocery_list:
                    if item_info["Item"] == self.item:
                        if item_info['Bought']:
                            print("\nThe item is already marked as bought")
                        else:
                            item_info["Bought"] = True
                            print(f"\nThe item {self.item} has been marked as bought")
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
            elif all(self.item != item_info["Item"] for item_info in self.grocery_list):
                print("\nNo such item found")
                break
            else:
                # Looping through each item information
                for item_info in self.grocery_list:
                    if item_info["Item"] == self.item:
                        if not item_info["Bought"]:
                            print("\nThe item is already not marked")
                            break
                        else:
                            item_info["Bought"] = False
                            print(f"\nThe item {self.item} has been unmarked")
                            break
                    else:
                        continue
                break
    # Creating the function that displays the total price
    def display_total_price(self):
        self.total_price = sum(item_info["Price"] for item_info in self.grocery_list)
        print("\nTotal price: ")
        # Check if grocery list data exists
        if not self.grocery_list:
            print("\nNo data found")
        else:
            print(f"{self.total_price:.2f}")
    # Creating the function that displays the amount of items found
    def display_amount_of_items(self):
        self.amount_of_items = sum(item_info["Amount"] for item_info in self.grocery_list)
        print("\nAmount of items: \n")
        # Check if grocery list data exists
        if not self.grocery_list:
            print("No data found")
        else:
            print(f"{self.amount_of_items}: ")
            # Looping through each item information
            for item_info in self.grocery_list:
                print(f"{item_info['Item']} = {item_info['Amount']}")
    # Creating the function that displays the total price according to a specific category
    def display_total_price_category(self):
        # Check if grocery list data exists
        if not self.grocery_list:
            print("\nNo data found to proceed")
        else:
            # Asking for the category while checking if its valid or found
            while True:
                self.category = input("Enter the category to show the total price ->: ").capitalize()
                if not self.category:
                    print("Enter a valid category")
                elif all(self.category != item_info["Category"] for item_info in self.grocery_list):
                    print("\nNo such category found")
                    break
                else:
                    self.total_price = sum(item_info["Price"] for item_info in self.grocery_list if item_info["Category"] == self.category)
                    print(f"\nTotal price({self.category}): ")
                    print(f"{self.total_price:.2f}")
                    break
    # Creating the function that displays the amount of items found according to a specific category
    def display_amount_of_items_category(self):
        # Check if grocery list data exists
        if not self.grocery_list:
            print("\nNo data found to proceed")
        else:
            # Asking for the category while checking if its valid or found
            while True:
                self.category = input("Enter the category to show the amount of items found ->: ").capitalize()
                if not self.category:
                    print("Enter a valid category")
                elif all(self.category != item_info["Category"] for item_info in self.grocery_list):
                    print("\nNo such category found")
                    break
                else:
                    self.amount_of_items = sum(item_info["Amount"] for item_info in self.grocery_list if item_info["Category"] == self.category)
                    print("\nThe amount of items found: \n")
                    print(f"{self.amount_of_items}: \n")
                    # Looping through each item information
                    for item_info in self.grocery_list:
                        if item_info["Category"] == self.category:
                            print(f"{item_info['Item']} = {item_info['Amount']}")
                        else:
                            continue
                    break
    # Creating the function that searchs for a specific item and displays its information
    def search_item_info(self):
        # Asking for the item while checking if its valid or found
        while True:
            self.item = input("Enter the item whose information you would like to see ->: ").capitalize()
            if not self.item:
                print("Enter a valid item")
            elif all(self.item != item_info["Item"] for item_info in self.grocery_list):
                print("\nNo such item found")
                break
            else:
                print(f"\n{self.item} item information: \n")
                # Looping through each item information
                for item_info in self.grocery_list:
                    if item_info["Item"] == self.item:
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
    # Creating the function that sets a budget and check if the list is enough for the total price  
    def set_budget_and_check(self):
        # Check if grocery list data exists
        if not self.grocery_list:
            print("\nNo data found to proceed")
        else:
            self.total_price = sum(item_info["Price"] for item_info in self.grocery_list)
            # Asking for the budget while checking if its valid or not
            while True:
                try:
                    self.budget = float(input("Enter the budget ->: "))
                    if self.budget <= 0:
                        print("Enter a valid budget that is bigger than 0")
                    else:
                        break
                except ValueError:
                    print("Invalid budget")
            # Check if the budget is good for the total price of the grcoery list
            if self.total_price > self.budget:
                print("\nThe budget is not enough you can enter a new one")
                # Looping through each item information
                for item_info in self.grocery_list:
                    if (self.total_price - item_info['Price']) <= self.budget:
                        print(f"or you can remove {item_info['Item']} and have {self.total_price - item_info['Price']} which will be enough for the budget")
                    else:
                        continue
            elif self.total_price == self.budget:
                print("\nIt is enough but you won't have any change left")
            else:
                print(f"\nIt is enough and you will have {self.budget - self.total_price} leftover")
    # Creating the function that displays item information according to a specific category
    def display_items_category(self):
        # Check if grocery list data exists
        if not self.grocery_list:
            print("\nNo data found to proceed")
        else:
            # Asking for the category while checking if its valid or found
            while True:
                self.category = input("Enter the category of the items that you would like to see ->: ").capitalize()
                if not self.category:
                    print("Enter a valid category")
                elif all(self.category != item_info["Category"] for item_info in self.grocery_list):
                    print("\nNo such category found")
                    break
                else:
                    print(f"\n{self.category} item information: ")
                    # Looping through each item information
                    for item_info in self.grocery_list:
                        if item_info["Category"] == self.category:
                            print() # <- this is for clearer structure to seperate each item information
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
                break
# Creating the class that is responsible for the CLI commands while inheriting most of the variables from the DigitalGroceryList class to avoid AttributeError's
class DigitalGroceryListCLI(DigitalGroceryList):
    # Creating the function that displays the options and asks the user what they want
    def display_menu(self):
        DigitalGroceryListData.read_data(self)
        print("--- Digital Grocery List ---")
        while True:
            print("\n1. Add a new item")
            print("2. View all items")
            print("3. Delete an item")
            print("4. Clear the grocery list")
            print("5. Edit an item's attribute(Name, Amount, Price, Category)")
            print("6. Mark an item as bought")
            print("7. Unmark an item")
            print("8. View total price")
            print("9. View amount of items found")
            print("10. View total price according to a specific category")
            print("11. View amount of items found according to a specific category")
            print("12. Search for an item's information")
            print("13. Set a budget and check if its enough")
            print("14. View all item information according to a specific category")
            print("15. Exit")
            self.option = input("Enter your choice(1-15) ->: ")
            if self.option == '1':
                DigitalGroceryList.add_new_item(self)
            elif self.option == '2':
                DigitalGroceryList.display_items(self)
            elif self.option == '3':
                DigitalGroceryList.delete_item(self)
            elif self.option == '4':
                DigitalGroceryList.clear_grocery_list(self)
            elif self.option == '5':
                DigitalGroceryList.edit_item_attribute(self)
            elif self.option == '6':
                DigitalGroceryList.mark_item(self)
            elif self.option == '7':
                DigitalGroceryList.unmark_item(self)
            elif self.option == '8':
                DigitalGroceryList.display_total_price(self)
            elif self.option == '9':
                DigitalGroceryList.display_amount_of_items(self)
            elif self.option == '10':
                DigitalGroceryList.display_total_price_category(self)
            elif self.option == '11':
                DigitalGroceryList.display_amount_of_items_category(self)
            elif self.option == '12':
                DigitalGroceryList.search_item_info(self)
            elif self.option == '13':
                DigitalGroceryList.set_budget_and_check(self)
            elif self.option == '14':
                DigitalGroceryList.display_items_category(self)
            elif self.option == '15':
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
# Creating the class that is responsible for the data saving
class DigitalGroceryListData:
    # Initializing one variable thats gonna be used in this class
    def __init__(self):
        self.grocery_list = []
    # Creating the function that reads the data from the file and writes it into the program
    def read_data(self):
        # Check if the file exists
        if Path("grocery_list.json").is_file():
            with open("grocery_list.json", "r") as f:
                self.grocery_list = json.load(f)
    # Creating the function that reads the data from the program and writes it into the file
    def write_data(self):
        with open("grocery_list.json", "w") as f:
            json.dump(self.grocery_list, f)
grocery_list = DigitalGroceryListCLI().display_menu()   
