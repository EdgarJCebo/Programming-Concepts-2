#Write a program asking the user for a list of their monthly expenses. When asking the user for their expenses, ask for
#the type of expense and the amount. Use the reduce method to analyze the expenses and display the total expense,
#the highest expense and the lowest expense. Label what the highest and lowest expense is.
#You can use separate functions for your calculations, or you can use lambda functions within your main function to do this.
from functools import reduce

#function to request the user to enter their expense type or finish the function
def get_expenses():
    expenses = []
    while True:
        expense_type = input("Please enter your expense type (or enter 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        try:
            amount = float(input(f"Enter amount for {expense_type}: $"))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Invalid amount. Please enter a number.")
    return expenses

#function that gets the expenses from the code above and stores the results
def main():
    expenses = get_expenses()

    if not expenses:
        print("No expenses entered.")
        return

    #Calculates the total using reduce
    total = reduce(lambda acc, x: acc + x[1], expenses, 0)

    #Finds the highest expense
    highest = reduce(lambda acc, x: x if x[1] > acc[1] else acc, expenses)

    #Finds the lowest expense
    lowest = reduce(lambda acc, x: x if x[1] < acc[1] else acc, expenses)

    print("\nExpense Summary:")
    print(f"Total Expense: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")

if __name__ == "__main__":
    main()