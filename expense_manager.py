from database import get_connection


def add_expense(title, amount, category, date):
    """
    Adds a new expense to the database.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO expenses (title, amount, category, date)
        VALUES (?, ?, ?, ?)
    """, (title, amount, category, date))

    connection.commit()

    connection.close()

    print("\nExpense added successfully!")


def get_all_expenses():
    """
    Returns all expenses.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, amount, category, date
        FROM expenses
        ORDER BY date DESC
    """)

    expenses = cursor.fetchall()

    connection.close()

    return expenses


def search_by_category(category):
    """
    Searches expenses by category.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, amount, category, date
        FROM expenses
        WHERE LOWER(category) = LOWER(?)
        ORDER BY date DESC
    """, (category,))

    expenses = cursor.fetchall()

    connection.close()

    return expenses


def calculate_total():
    """
    Calculates total expenses.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
    """)

    total = cursor.fetchone()[0]

    connection.close()

    return total


def calculate_monthly_expenses(year, month):
    """
    Calculates expenses for a particular month.
    """

    month_string = f"{year:04d}-{month:02d}"

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE substr(date, 1, 7) = ?
    """, (month_string,))

    total = cursor.fetchone()[0]

    connection.close()

    return total


def calculate_yearly_expenses(year):
    """
    Calculates expenses for a particular year.
    """

    year_string = str(year)

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE substr(date, 1, 4) = ?
    """, (year_string,))

    total = cursor.fetchone()[0]

    connection.close()

    return total


def delete_expense(expense_id):
    """
    Deletes an expense using its ID.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM expenses
        WHERE id = ?
    """, (expense_id,))

    deleted_rows = cursor.rowcount

    connection.commit()

    connection.close()

    return deleted_rows

