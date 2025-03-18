from stats import count_words, char_count, sorted_list_dictionary
import sys

def get_book_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()
def print_report(file_path, word_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["character"].isalpha():
            character = item["character"]
            count = item["count"]
            print(f"{character}: {count}")
    print("============= END ===============")



def main():
    file_path = None
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]

    frankenstein = get_book_text(file_path)
    word_count = count_words(frankenstein)
    char_counts = char_count(frankenstein)
    sorted_list = sorted_list_dictionary(char_counts)
    print_report(file_path, word_count, sorted_list)
    
    

main()
    
