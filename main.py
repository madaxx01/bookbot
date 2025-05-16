from stats import get_num_words
from stats import get_char_count
from stats import get_sorted_char_count
import sys

# main.py
def get_book_text(filepath):

    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()  

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    # Check if the file exists
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            pass
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        sys.exit(1)

    book_text = get_book_text(filepath)
    print("======================BOOKBOT======================")
    print(f"Analyzing book found at {filepath}")
    print("---------------------Word Count---------------------")
    print(f"Found {get_num_words(book_text)} total words")
    print("---------------------Character Count---------------------")
    char_dict = get_char_count(book_text)
    char_counts = get_sorted_char_count(char_dict)

    # Print only alphabetic characters and their counts
    for item in char_counts:
        print(f"{item}: {char_dict.get(item, 0)}")
            
    print("---------------------END---------------------")
    
if __name__ == "__main__":
    main()