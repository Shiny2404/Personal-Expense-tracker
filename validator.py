from datetime import datetime


def validate_title(title):
    """
    Validates expense title.
    """

    title = title.strip()

    if not title:
        print("Title cannot be empty.")
        return False

    return True


def validate_amount(amount):
    """
    Validates expense amount.
    """

    try:
        amount = float(amount)

        if amount <= 0:
            print("Amount must be greater than 0.")
            return False

        return True

    except ValueError:
        print("Please enter a valid number.")

        return False


def validate_category(category):
    """
    Validates expense category.
    """

    category = category.strip()

    if not category:
        print("Category cannot be empty.")
        return False

    return True


def validate_date(date):
    """
    Validates date in YYYY-MM-DD format.
    """

    try:

        datetime.strptime(date, "%Y-%m-%d")

        return True

    except ValueError:

        print("Invalid date.")
        print("Please use YYYY-MM-DD format.")

        return False