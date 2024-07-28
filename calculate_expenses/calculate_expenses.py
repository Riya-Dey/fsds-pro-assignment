# calculate_expenses.py

def calculate_total_expenses(file_path):
    """
    Reads an expense file and calculates the total amount spent.

    Parameters:
    file_path (str): The path to the expense file.

    Returns:
    float: The total amount spent.
    """
    total = 0.0
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    # Split the line into category and amount
                    category, amount_str = line.split(':')
                    amount = float(amount_str.strip())
                    total += amount
                except ValueError:
                    print(f"Warning: Skipping invalid line: '{line}'")
    
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
    
    return total

def main():
    # File path
    file_path = 'calculate_expenses/expenses.txt'
    
    # Calculate the total expenses
    total_expenses = calculate_total_expenses(file_path)
    
    # Display the total expenses
    print(f"Total expenses: ${total_expenses:.2f}")

if __name__ == "__main__":
    main()
