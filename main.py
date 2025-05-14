
# main.py
def get_book_text(filepath):

    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()  
def count_words(text):  
    words = text.split()
    return len(words)
    

def main():
    filepath = 'books/frankenstein.txt'
    book_text = get_book_text(filepath)
    print(f"{count_words(book_text)} words found in the document")
    
if __name__ == "__main__":
    main()