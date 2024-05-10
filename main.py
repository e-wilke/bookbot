def count_words_and_letters(text):
    #split the text into words using whitespace
    words = text.split()
    #count the number of words
    word_count = len(words)
    
    #count the occurrence of each leter
    letter_count ={}
    for char in text:
        if char.isalpha(): #see if the character is a letter
            char = char.lower() # make it a lower case letter
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return word_count, letter_count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # Call count_words_and_letters fuction to count the words and letters in the text
        num_words, letter_counts = count_words_and_letters(file_contents)
        print ("Number of words in Frankenstein is", num_words)
        print ("letter counts:")
        # Convert dictionary to a list of tuples and sort it alphabetically
        sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[0])
        for letter, count in sorted_letter_counts:
            print(f"{letter}: {count}")       

if __name__ == "__main__":
    main()