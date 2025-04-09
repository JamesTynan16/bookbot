import sys
from stats import get_word_count
from stats import get_character_count
from stats import sorted_character_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        print(f"{get_word_count(get_book_text(sys.argv[1]))} words found in the document")
        character_count = get_character_count(get_book_text(sys.argv[1]))
        sorted = sorted_character_list(character_count)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {get_word_count(get_book_text(sys.argv[1]))} total words")
        print("--------- Character Count -------")
        for i in range(0,len(sorted)):
            if sorted[i]["character"].isalpha():
                print(f"{sorted[i]["character"]}: {sorted[i]["count"]}")

main()