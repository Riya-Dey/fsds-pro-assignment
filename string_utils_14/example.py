# example_usage.py

from string_utils import reverse_string, capitalize_string, upper_case_string, lower_case_string

def main():
    sample_string = "hello world"
    
    print("Original:", sample_string)
    print("Reversed:", reverse_string(sample_string))
    print("Capitalized:", capitalize_string(sample_string))
    print("Uppercase:", upper_case_string(sample_string))
    print("Lowercase:", lower_case_string(sample_string))

if __name__ == "__main__":
    main()
