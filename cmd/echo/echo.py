import argparse


def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="making echo")
    # Add a positional argument
    parser.add_argument('message', type=str, help="The message to print")
    # Add an optional argument
    parser.add_argument('-n', action='store_true', help="Do not print the trailing newline character")
    args = parser.parse_args()
    # Print the message
    if args.n:
        print(args.message, end='')
    else:
        print(args.message)


if __name__ == "__main__":
    main()
