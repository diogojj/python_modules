import sys


def main() -> None:
    """Display the command-line parameters received by the program."""
    args: list[str] = sys.argv
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")
    if len(args) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args) - 1}")
        position: int = 1
        for value in args[1:]:
            print(f"Argument {position}: {value}")
            position += 1
    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    main()
