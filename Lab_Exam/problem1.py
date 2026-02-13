# Author: Sachin
# Description: A command line shopping list manager with file persistence

class ShoppingList:
    """A class to manage a persistent shopping list."""
    
    def __init__(self, filename="shopping_list.txt"):
        """Initialize state and load items from file."""
        self.filename = filename
        self.items = []
        self.load_items()
    
    def load_items(self):
        """Read items from the file into memory."""
        try:
            with open(self.filename, 'r') as f:
                self.items = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            self.items = []
        except IOError as e:
            print(f"Error loading file: {e}")
            self.items = []
    
    def save_items(self):
        """Write the list to the file."""
        try:
            with open(self.filename, 'w') as f:
                for item in self.items:
                    f.write(item + '\n')
        except IOError as e:
            print(f"Error saving file: {e}")
    
    def start_menu(self):
        """Print the menu/instructions."""
        print("What do you want to add to your shopping list?")
        print("Enter 'DONE' to stop adding items.")
        print("Enter 'HELP' for additional info.")
        print("Enter 'SHOW' to see your shopping list.")
        print("Enter 'REMOVE' to remove an item from your shopping list.")
        print("-" * 41)
    
    def add_to_list(self, item):
        """Add a single item (case normalized) if not already present."""
        normalized_item = item.capitalize()
        if normalized_item in self.items:
            print(f"{normalized_item} is already on your shopping list.")
        else:
            self.items.append(normalized_item)
            print(f"{normalized_item} was added to your shopping list.")
        print(f"You have {len(self.items)} items on your list.")
    
    def remove_item(self, item):
        """Remove a single item if present."""
        normalized_item = item.capitalize()
        if normalized_item in self.items:
            self.items.remove(normalized_item)
            print(f"{normalized_item} was removed from your shopping list.")
        else:
            print(f"{normalized_item} was not found on your shopping list.")
        print(f"You have {len(self.items)} items on your list.")
    
    def show_shopping_list(self):
        """Print the current list."""
        print("My Shopping List:")
        if not self.items:
            print("(empty)")
        else:
            for item in self.items:
                print(f"- {item}")


def main():
    """Main function to run the shopping list application."""
    shopping_list = ShoppingList()
    shopping_list.start_menu()
    
    while True:
        try:
            user_input = input("> ").strip()
            
            if not user_input:
                continue
            
            command = user_input.upper()
            
            if command == "DONE":
                print("See you soon!")
                shopping_list.save_items()
                print("Your shopping list has been saved.")
                shopping_list.show_shopping_list()
                break
            
            elif command == "HELP":
                shopping_list.start_menu()
            
            elif command == "SHOW":
                shopping_list.show_shopping_list()
            
            elif command == "REMOVE":
                shopping_list.show_shopping_list()
                try:
                    item_to_remove = input("What do you want to remove?: ").strip()
                    if item_to_remove:
                        shopping_list.remove_item(item_to_remove)
                except EOFError:
                    print("\nSee you soon!")
                    shopping_list.save_items()
                    print("Your shopping list has been saved.")
                    break
            
            else:
                # Treat as item to add
                shopping_list.add_to_list(user_input)
        
        except EOFError:
            print("\nSee you soon!")
            shopping_list.save_items()
            print("Your shopping list has been saved.")
            break


if __name__ == '__main__':
    main()
