import argparse
import sys


def check(error):
    if error is not None:
        sys.exit(str(error))


# Validate the arguments of the wc command
def wc_arguments_validator():
    parser = argparse.ArgumentParser(description="Wc command in python")
    parser.add_argument('file', type=str, help="The file to read from")
    parser.add_argument('-l', action='store_true', help="Print the number of lines in the file")
    parser.add_argument('-w', action='store_true', help="Print the number of words in the file")
    parser.add_argument('-c', action='store_true', help="Print the number of characters in the file")

    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.error("Incorrect number of arguments")

    return args.file, args.l, args.w, args.c


# Count the number of lines, words, and characters in a file
def count(file_name):
    lines = 0
    words = 0
    characters = 0
    try:
        with open(file_name, 'r') as f:
            for line in f:
                lines += 1
                words += len(line.split())
                characters += len(line)
    except Exception as e:
        return str(e)

    return lines, words, characters


def main():
    file_path, number_of_lines, number_of_words, number_of_characters = wc_arguments_validator()
    lines, words, characters = count(file_path)
    # If no options are provided, print all the counts
    if not number_of_lines and not number_of_words and not number_of_characters:
        print(lines, words, characters)
        sys.exit(0)
    if number_of_lines:
        print(lines, end=' ')
    if number_of_words:
        print(words, end=' ')
    if number_of_characters:
        print(characters, end=' ')


if __name__ == "__main__":
    main()
