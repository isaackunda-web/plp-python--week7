# shopping_list.py

# 1. Start with an empty list
shopping_list = []

# 2. Use a loop to show a menu again and again
while True:
    choice = input("\nWould you like to (add / remove / show / done)? ").strip().lower()
    
    if choice == "add":
        item = input("Enter the item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(f"'{item}' has been added.")
            
    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()
        # Check if item is in the list before removing to prevent crashes
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed.")
        else:
            print("That item is not on your list.")
            
    elif choice == "show":
        print("\n--- Your Shopping List ---")
        if not shopping_list:
            print("Your list is currently empty.")
        else:
            for item in shopping_list:
                print(f"- {item}")
        print("--------------------------")
            
    elif choice == "done":
        print("Goodbye! Have a wonderful day.")
        break
        
    else:
        print("Invalid choice. Please type add, remove, show, or done.")