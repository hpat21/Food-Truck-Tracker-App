from datetime import datetime


def convert_date_to_desired_format(date_string):
    """
    Converts the date string to the desired format.
    If the date string is in YYYYMMDD format -
    or MM/DD/YYYY HH:MM:SS AM/PM format, converts it to YYYY-MM-DD format.
    """

    try:
        date_obj = datetime.strptime(date_string, "%Y%m%d")
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        pass

    try:
        date_obj = datetime.strptime(date_string, "%m/%d/%Y %I:%M:%S %p")
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        pass


def convert_decimal_format(value):
    """
    Converts the input value to a specific decimal format.
    If the input value has more than 7 characters and
    doesn't contain a decimal point, converts it to a format -
    with 7 digits before the decimal point.
    """

    if not value:
        return None

    value_str = str(value)

    if len(value_str) > 7 and "." not in value_str:
        integer_part = value_str[:-2]
        decimal_part = value_str[-2:]
        value_str = f"{integer_part}.{decimal_part}"

    return float(value_str)


def fix_empty_value(value):
    """
    Fixes empty values by returning None -if the input value is empty.
    """

    if not value:
        return None

    return value
