# example_usage.py

from file_operations import read_file, write_file, append_to_file

def main():
    file_path = 'file_operations/example.txt'
    
    # Write to file
    write_file(file_path, 'Hello, world!\n')
    print("File written.")
    
    # Append to file
    append_to_file(file_path, 'Appending some more text.\n')
    print("Content appended.")
    
    # Read from file
    content = read_file(file_path)
    print("File content:")
    print(content)

if __name__ == "__main__":
    main()
