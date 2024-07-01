import argparse
import sys


def check(error):
    if error is not None:
        sys.exit(str(error))


def cat_arguments_validator():
    # Create the parser
    parser = argparse.ArgumentParser(description="Print the lines in the file")
    # Add the arguments
    parser.add_argument('file', type=str, help="The file to read from")
    parser.add_argument('-n', action='store_true', help="Number of line will be printed from the beginning "
                                                        "of line")

    args = parser.parse_args()
    # Check if the number of arguments is correct
    if len(sys.argv) < 2:
        parser.error("Incorrect number of arguments")

    return args.file, args.n


# Print the file
def print_file(file_name, line_number):
    try:
        with open(file_name, 'r') as f:
            for i, line in enumerate(f):
                # Check if the line number is required
                if line_number:
                    print(i + 1, end=' ')
                print(line, end='')

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read file '{file_name}'")
    except Exception as e:
        print(f"Error: {e}")

    print("\n")
    return None


def main():
    file_path, line_number = cat_arguments_validator()
    error = print_file(file_path, line_number)
    check(error)


if __name__ == "__main__":
    main()
