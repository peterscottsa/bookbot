from stats import get_word_count, get_character_count, get_sorted_char_list
import sys


def get_book_text(filepath):
  with open(filepath, 'r') as file:
    return file.read()

def main():
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  book_text = get_book_text('books/frankenstein.txt')
  print("----------- Word Count ----------")
  num_words = get_word_count(book_text)
  print(f"Found {num_words} total words")
  print("----------- Character Count ----------")
  char_count = get_character_count(book_text)
  sorted_list = get_sorted_char_list(char_count)
  
  for item in sorted_list:
    print(f"{item['char']}: {item['num']}")

  print("============= END ===============")

main()
