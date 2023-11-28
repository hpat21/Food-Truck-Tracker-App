from datetime import datetime

def convert_date_to_desired_format(date_string):
    # Check if the date string is in YYYYMMDD format
    try:
        date_obj = datetime.strptime(date_string, '%Y%m%d')
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        pass
    
    # Check if the date string is in MM/DD/YYYY HH:MM:SS AM/PM format
    try:
        date_obj = datetime.strptime(date_string, '%m/%d/%Y %I:%M:%S %p')
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        pass


def convert_decimal_format(value):
    if not value:  # Check if the value is empty (empty string or None)
        return None  # Return None if the value is empty
    
    value_str = str(value)  # Convert the value to a string

    # If the length is greater than 7 and the value isn't already in the desired format
    if len(value_str) > 7 and '.' not in value_str:
        integer_part = value_str[:-2]  # Retrieve the integer part
        decimal_part = value_str[-2:]  # Retrieve the last two digits as the decimal part
        value_str = f"{integer_part}.{decimal_part}"  # Reconstruct the value with a decimal point

    return float(value_str)

def fix_empty_value(value):
    if not value:  # Check if the value is empty (empty string or None)
        return None  # Return None if the value is empty
    
    return value

    