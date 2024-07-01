import argparse
import os
import sys


def check(error):
    if error is not None:
        sys.exit(str(error))


# Validate the arguments
def tree_arguments_validator():
    parser = argparse.ArgumentParser(description="Print the tree of a directory")
    parser.add_argument('dir', type=str, help="The path of directory")
    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.error("Incorrect number of arguments")

    return args.dir


# Print the tree of the directory
def print_tree(dir_path, level):
    try:
        with os.scandir(dir_path) as entries:
            for entry in entries:
                # Print the spaces
                print(" " * level, end='')
                # Print the name of the entry
                if level > 0:
                    print("|--", end='')
                print(entry.name)
                if entry.is_dir():
                    # Recursion
                    print_tree(entry.path, len(entry.name))

    except FileNotFoundError:
        return f"Error: Directory '{dir_path}' not found."
    except PermissionError:
        return f"Error: Permission denied to read directory '{dir_path}'"
    except Exception as e:
        return f"Error: {e}"
    return None


def main():
    dir_path = tree_arguments_validator()
    error = print_tree(dir_path, 0)
    check(error)


if __name__ == "__main__":
    main()
