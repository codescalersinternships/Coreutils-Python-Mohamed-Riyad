import argparse
import sys


def check(error):
    if error is not None:
        sys.exit(str(error))


def head_arguments_validator():
    # create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Print the head of a file")
    # add the file argument
    parser.add_argument('file', type=str, help="The file to read from")
    # add the number of lines argument
    parser.add_argument('-n', type=int, default=10, help="Number of lines to print from the beginning of the file")

    args = parser.parse_args()

    # check if the number of arguments is not less than 2
    if len(sys.argv) < 2:
        parser.error("Incorrect number of arguments")

    return args.file, args.n


def print_lines_head(file_name, num_lines):
    try:
        with open(file_name, 'r') as f:
            for i, line in enumerate(f):
                # print the line if the line number is less than the number of required lines
                if i < num_lines:
                    print(line, end='')
                else:
                    break
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read file '{file_name}'")
    except Exception as e:
        print(f"Error: {e}")
    print("\n")
    return None


def main():
    file_path, num_lines = head_arguments_validator()
    error = print_lines_head(file_path, num_lines)
    check(error)


if __name__ == "__main__":
    main()
