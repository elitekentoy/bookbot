from stats import get_num_words
from stats import get_occurence_count
from stats import sort
import sys

if 2 != len(sys.argv):
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)


def get_book_text(path_to_file):
	print(f"Analyzing book found at {path_to_file}")
	with open(path_to_file) as file:
		contents = file.read()
	return contents


def main(path_to_file):
	print("============ BOOKBOT ============")
	frankenstein = get_book_text(path_to_file)
	num_words = get_num_words(frankenstein)
	occurence = get_occurence_count(frankenstein)
	sorted = sort(occurence)

	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")

	print("--------- Character Count -------")
	for each in sorted:
		character = each["character"]

		if character.isalpha():
			print(f"{character}: {each["count"]}")

path = sys.argv[1]
main(path)
