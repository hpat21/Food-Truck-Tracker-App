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
    value_str = str(value)  # Convert the value to a string

    # If the length is greater than 7, truncate the excess and add decimal point
    if len(value_str) > 7:
        value_str = value_str[:-2]  # Remove excess digits from the end
        value_str = value_str[:-5] + '.' + value_str[-5:]  # Insert the decimal point

    return float(value_str) 
    