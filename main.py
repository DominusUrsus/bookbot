#Import word_counter, char_counter, stats_sorter functions from stats.py
from stats import word_counter, char_counter, stats_sorter
#import sys module
import sys

#verify length of input is correct (that there is a filepath)
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

#read filepath from args
file_path = f"{sys.argv[1]}"

#Read the provided *.txt file
def get_book_text(file_path):
    #with block to read the *.txt file
    with open(file_path) as file:
        file_contents = file.read()

    return file_contents

def main():
    file_contents = get_book_text(file_path)
    sort_count = char_counter(file_contents)
    print(f"============ BOOKBOT ============ \nAnalyzing book found at {file_path}...")
    print(f"----------- Word Count ---------- \nFound {word_counter(file_contents)} total words")
    print("--------- Character Count -------")
    sorted_chars_list = stats_sorter(sort_count)
    for item in sorted_chars_list:
        char = item["char"]
        count = item["num"]
        print(f"{char}: {count}")

    print("============= END ===============")

main()