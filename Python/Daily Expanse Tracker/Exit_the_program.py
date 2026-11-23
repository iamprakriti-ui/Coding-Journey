print("Welcome to the Daily Expense Tracker!")

# Display menu once
print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

while True:
    # Get user choice
    choice = input()

    if choice == "5":
        # Exit the program
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
