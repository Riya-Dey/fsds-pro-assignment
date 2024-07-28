# word_count.py

from collections import Counter
import re

def count_words(file_path):
    """
    Reads a text file and counts the occurrences of each word.
    
    Parameters:
    file_path (str): The path to the text file.
    
    Returns:
    dict: A dictionary where the keys are words and values are their counts.
    """
    word_count = Counter()
    
    try:
        with open(file_path, 'r') as file:
            # Read the entire file content
            content = file.read()
            
            # Use regular expression to find words
            words = re.findall(r'\b\w+\b', content.lower())
            
            # Update word counts
            word_count.update(words)
    
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
    
    return dict(word_count)

def display_word_counts(word_counts):
    """
    Displays word counts in alphabetical order.
    
    Parameters:
    word_counts (dict): A dictionary with words and their counts.
    """
    for word in sorted(word_counts):
        print(f"{word}: {word_counts[word]}")

def main():
    # File path
    file_path = 'paragraph/paragraph.txt'
    
    # Count the words
    word_counts = count_words(file_path)
    
    # Display the word counts
    display_word_counts(word_counts)

if __name__ == "__main__":
    main()
