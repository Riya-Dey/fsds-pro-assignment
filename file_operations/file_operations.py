# file_operations.py

def read_file(file_path):
    """
    Reads the content of a file.

    Parameters:
    file_path (str): The path to the file to read.

    Returns:
    str: The content of the file.

    Raises:
    FileNotFoundError: If the file does not exist.
    IOError: If there is an error reading the file.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")

def write_file(file_path, content):
    """
    Writes content to a file, overwriting any existing content.

    Parameters:
    file_path (str): The path to the file to write.
    content (str): The content to write to the file.

    Raises:
    IOError: If there is an error writing to the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError as e:
        raise IOError(f"An error occurred while writing to the file: {e}")

def append_to_file(file_path, content):
    """
    Appends content to a file.

    Parameters:
    file_path (str): The path to the file to append to.
    content (str): The content to append to the file.

    Raises:
    IOError: If there is an error appending to the file.
    """
    try:
        with open(file_path, 'a') as file:
            file.write(content)
    except IOError as e:
        raise IOError(f"An error occurred while appending to the file: {e}")
