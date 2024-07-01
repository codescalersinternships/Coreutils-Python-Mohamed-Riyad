import argparse
import sys


def check(error):
    if error is not None:
        sys.exit(str(error))


def tail_arguments_validator():
    # Create the parser
    parser = argparse.ArgumentParser(description="Print the tail of a file")
    # Add the arguments
    parser.add_argument('file', type=str, help="The file to read from")
    parser.add_argument('-n', type=int, default=10, help="Number of lines to print from the beginning of the file")

    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.error("Incorrect number of arguments")

    return args.file, args.n


def print_lines_tail(file_name, num_lines):
    # Read the file and print the last num_lines lines
    lines = []
    try:
        with open(file_name, 'r') as f:
            for i, line in enumerate(f):
                lines.append(line)
                # If the number of lines exceeds num_lines, remove the first line
                if len(lines) > num_lines:
                    lines.pop(0)
    except FileNotFoundError:
        return f"Error: File '{file_name}' not found."
    except PermissionError:
        return f"Error: Permission denied to read file '{file_name}'"
    except Exception as e:
        return f"Error: {e}"
    # Print the lines
    for line in lines:
        print(line, end='')
    print("\n")
    return None


def main():
    file_path, num_lines = tail_arguments_validator()
    error = print_lines_tail(file_path, num_lines)
    check(error)


if __name__ == "__main__":
    main()
