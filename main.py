from datetime import date

from database import create_database

from expense_manager import (
    add_expense,
    get_all_expenses,
    search_by_category,
    calculate_total,
    calculate_monthly_expenses,
    calculate_yearly_expenses,
    delete_expense
)

from validator import (
    validate_title,
    validate_amount,
    validate_category,
    validate_date
)


def display_expenses(expenses):
    """
    Displays expenses in a readable format.
    """

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n" + "=" * 75)
    print(
        f"{'ID':<5}"
        f"{'Title':<20}"
        f"{'Amount':<12}"
        f"{'Category':<18}"
        f"{'Date':<12}"
    )
    print("=" * 75)

    for expense in expenses:

        expense_id, title, amount, category, expense_date = expense

        print(
            f"{expense_id:<5}"
            f"{title:<20}"
            f"₹{amount:<11.2f}"
            f"{category:<18}"
            f"{expense_date:<12}"
        )

    print("=" * 75)


def add_new_expense():

    print("\n========== Add New Expense ==========")

    while True:

        title = input("Enter expense title: ")

        if validate_title(title):
            break

    while True:

        amount = input("Enter amount: ")

        if validate_amount(amount):
            amount = float(amount)
            break

    while True:

        category = input("Enter category: ")

        if validate_category(category):
            break

    while True:

        expense_date = input(
            "Enter date (YYYY-MM-DD) "
            "[Press Enter for today]: "
        )

        if not expense_date:
            expense_date = str(date.today())
            break

        if validate_date(expense_date):
            break

    add_expense(
        title,
        amount,
        category,
        expense_date
    )


def view_all_expenses():

    print("\n========== All Expenses ==========")

    expenses = get_all_expenses()

    display_expenses(expenses)


def search_expenses():

    print("\n========== Search Expenses ==========")

    category = input("Enter category: ")

    expenses = search_by_category(category)

    display_expenses(expenses)


def show_total_expenses():

    print("\n========== Total Expenses ==========")

    total = calculate_total()

    print(f"Total Expenses: ₹{total:.2f}")


def show_monthly_expenses():

    print("\n========== Monthly Expenses ==========")

    try:

        year = int(input("Enter year (YYYY): "))

        month = int(input("Enter month (1-12): "))

        if month < 1 or month > 12:

            print("Month must be between 1 and 12.")

            return

        total = calculate_monthly_expenses(
            year,
            month
        )

        print(
            f"Total expenses for "
            f"{year}-{month:02d}: ₹{total:.2f}"
        )

    except ValueError:

        print("Please enter valid numbers.")


def show_yearly_expenses():

    print("\n========== Yearly Expenses ==========")

    try:

        year = int(input("Enter year (YYYY): "))

        total = calculate_yearly_expenses(year)

        print(
            f"Total expenses for {year}: "
            f"₹{total:.2f}"
        )

    except ValueError:

        print("Please enter a valid year.")


def remove_expense():

    print("\n========== Delete Expense ==========")

    try:

        expense_id = int(
            input("Enter expense ID to delete: ")
        )

        deleted = delete_expense(expense_id)

        if deleted:

            print("Expense deleted successfully!")

        else:

            print("Expense ID not found.")

    except ValueError:

        print("Please enter a valid ID.")


def display_menu():

    print("\n")
    print("========================================")
    print("          PERSONAL EXPENSE TRACKER")
    print("========================================")

    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Search Expenses by Category")
    print("4. Calculate Total Expenses")
    print("5. Calculate Monthly Expenses")
    print("6. Calculate Yearly Expenses")
    print("7. Delete an Expense")
    print("8. Exit")

    print("========================================")


def main():

    create_database()

    while True:

        display_menu()

        choice = input("Enter your choice (1-8): ")

        try:

            if choice == "1":

                add_new_expense()

            elif choice == "2":

                view_all_expenses()

            elif choice == "3":

                search_expenses()

            elif choice == "4":

                show_total_expenses()

            elif choice == "5":

                show_monthly_expenses()

            elif choice == "6":

                show_yearly_expenses()

            elif choice == "7":

                remove_expense()

            elif choice == "8":

                print("\nThank you for using")
                print("Personal Expense Tracker!")

                break

            else:

                print("\nInvalid choice.")
                print("Please select a number between 1 and 8.")

        except Exception as error:

            print("\nSomething went wrong.")
            print(f"Error: {error}")


if __name__ == "__main__":
    main()