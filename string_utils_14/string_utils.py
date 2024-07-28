# string_utils.py

def reverse_string(s):
    """
    Reverses the given string.

    Parameters:
    s (str): The string to reverse.

    Returns:
    str: The reversed string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return s[::-1]

def capitalize_string(s):
    """
    Capitalizes the first letter of each word in the given string.

    Parameters:
    s (str): The string to capitalize.

    Returns:
    str: The capitalized string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return s.title()

def upper_case_string(s):
    """
    Converts all characters in the given string to uppercase.

    Parameters:
    s (str): The string to convert.

    Returns:
    str: The uppercase string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return s.upper()

def lower_case_string(s):
    """
    Converts all characters in the given string to lowercase.

    Parameters:
    s (str): The string to convert.

    Returns:
    str: The lowercase string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return s.lower()
