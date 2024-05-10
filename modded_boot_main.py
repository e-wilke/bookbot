def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    
    # Convert dictionary to a list of tuples
    chars_list = list(chars_dict.items())
    
    # Sort the list based on the second element of each tuple (the count)
    sorted_chars_list = sorted(chars_list, key=lambda x: x[1], reverse=True)
    
    print(sorted_chars_list)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
