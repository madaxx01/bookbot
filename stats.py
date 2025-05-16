def get_num_words(text):  
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def get_sorted_char_count(char_count):
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    sorted_char_count = {char: count for char, count in sorted_char_count if char.isalpha()}  

    return sorted_char_count