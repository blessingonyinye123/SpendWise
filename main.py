import database

def main():
    database.init_db()
    
    while True:
        print("\n=== PERSONAL EXPENSE TRACKER ===")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. View total spending")
        print("4. Delete an expense by ID")
        print("5. Clear all expenses")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            print("\n--- Add Expense ---")
            title = input("Enter expense title (e.g., Groceries): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category (e.g., Food, Transport): ")
            date = input("Enter date (YYYY-MM-DD): ")
            
            database.add_expense(title, amount, category, date)
            print("Success! Your expense has been recorded.\n")
            
        elif choice == "2":
            print("\n=== ALL RECORDED EXPENSES ===")
            all_expenses = database.get_expenses()
            
            if not all_expenses:
                print("No expenses recorded yet.\n")
            else:
                for expense in all_expenses:
                    print(f"ID: {expense[0]} | Title: {expense[1]} | Amount: {expense[2]} | Category: {expense[3]} | Date: {expense[4]}")
                print()
                
        elif choice == "3":
            total = database.get_total_spending()
            print(f"\n💰 Total Spending: {total:.2f}\n")
            
        elif choice == "4":
            print("\n--- Delete Expense ---")
            expense_id = input("Enter the ID of the expense you want to delete: ").strip()
            database.delete_expense(expense_id)
            print(f"Expense with ID {expense_id} has been deleted (if it existed).\n")
            
        elif choice == "5":
            confirm = input("Are you sure you want to clear all expenses? (y/n): ").strip().lower()
            if confirm == 'y':
                database.clear_expenses()
                print("All expenses have been cleared and IDs reset!\n")
            else:
                print("Clear action cancelled.\n")
                
        elif choice == "6":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    main()