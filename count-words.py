import sys
from collections import Counter
import re

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()  # Reads the input file and converts text to lowercase

    # Remove punctuations, special characters and numbers, keeping only letters and spaces
    text = re.sub(r'[^a-z\s]', '', text)
    
    words = text.split()  # Split the text into words

    # Counts every word occurrency
    word_counts = Counter(words)

    # Group the words into two lists: one with 4 or more characters and other with 3 or less
    words_4_or_more = {word: count for word, count in word_counts.items() if len(word) >= 4}
    words_3_or_less = {word: count for word, count in word_counts.items() if len(word) <= 3}

    # Order the words by occurrency quantity in descending order
    sorted_words_4_or_more = sorted(words_4_or_more.items(), key=lambda x: x[1], reverse=True)
    sorted_words_3_or_less = sorted(words_3_or_less.items(), key=lambda x: x[1], reverse=True)

    return sorted_words_4_or_more, sorted_words_3_or_less

def save_results(file_path, words_4_or_more, words_3_or_less):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("WORDS WITH 4 OR MORE CHARACTERS:\n \n")
        for word, count in words_4_or_more:
            file.write(f"{word}: {count}\n")
        
        file.write("\nWORDS WITH 3 OR LESS CHARACTERS:\n \n")
        for word, count in words_3_or_less:
            file.write(f"{word}: {count}\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: python count_words.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    sorted_words_4_or_more, sorted_words_3_or_less = process_file(input_file_path)
    save_results(output_file_path, sorted_words_4_or_more, sorted_words_3_or_less)

    print(f"Results saved in {output_file_path}")

if __name__ == "__main__":
    main()
