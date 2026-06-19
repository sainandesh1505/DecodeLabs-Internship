def expense_tracker():
    total_spent = 0
    print("--- Expense Tracker ---")
    print("Enter your expenses one by one. Type 'done' to see your total.")

    while True:
        user_input = input("Enter expense amount: ")

        if user_input.lower() == 'done':
            break
        
        try:
            # Convert input to a float to allow decimal amounts
            expense = float(user_input)
            
            # The Accumulator Pattern
            total_spent = total_spent + expense
            
            print(f"Added: {expense}")
        except ValueError:
            print("Invalid input. Please enter a numeric value or 'done'.")

    print("-" * 25)
    print(f"Total Spent: {total_spent}")
    print("--- Session Ended ---")

# Run the function
if __name__ == "__main__":
    expense_tracker()
