#Explore the power of Lambda Functions by creating an expense tracker.#
#learning summary:
#1. lambda x: expression, a concise way to represent a function that can take any number of arguments, but can only have one expression.
#2. map(function, iterable), applies a given function to all items in an input list (or any iterable).
#3. The filter() function constructs an iterator from elements of an iterable for which a function returns true.
#4. while True: creates an infinite loop that continues until a break statement is encountered.
#5. f-string is a way to create strings that can directly include variables or expressions inside the string.
#6. if and elif practice.

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f"Amount: {expense['amount']}, Category: {expense['category']}")
        #f-string is a way to create strings that can directly include variables or expressions inside the string#

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break

main()
