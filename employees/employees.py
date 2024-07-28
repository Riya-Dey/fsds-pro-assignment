# create_employees_file.py

def write_employee_data(file_path, employees):
    """
    Writes employee details to a text file.

    Parameters:
    file_path (str): The path to the file where employee details will be written.
    employees (list of dict): A list of dictionaries containing employee details.
    """
    try:
        with open(file_path, 'w') as file:
            for employee in employees:
                name = employee.get('name', 'Unknown')
                age = employee.get('age', 'Unknown')
                salary = employee.get('salary', 'Unknown')
                file.write(f"Name: {name}, Age: {age}, Salary: {salary}\n")
        print(f"Employee details have been written to {file_path}.")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    # Define employee details
    employees = [
        {'name': 'John Doe', 'age': 30, 'salary': 50000},
        {'name': 'Jane Smith', 'age': 28, 'salary': 55000},
        {'name': 'Alice Johnson', 'age': 35, 'salary': 60000},
        {'name': 'Bob Brown', 'age': 40, 'salary': 65000}
    ]

    # File path
    file_path = 'employees/employees.txt'
    
    # Write employee data to file
    write_employee_data(file_path, employees)

if __name__ == "__main__":
    main()
