# read_inventory.py

def read_file_line_by_line(file_path):
    """
    Reads and displays the contents of a file line by line.

    Parameters:
    file_path (str): The path to the file to read.

    Raises:
    FileNotFoundError: If the file does not exist.
    IOError: If there is an error reading the file.
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())  # Use strip() to remove any trailing newline characters
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")

def main():
    # File path
    file_path = 'reading_existing_txt_file/inventory.txt'
    
    # Read and display the contents of the file
    read_file_line_by_line(file_path)

if __name__ == "__main__":
    main()
