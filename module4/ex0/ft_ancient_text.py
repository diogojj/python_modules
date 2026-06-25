import sys
import typing


def recover(filename: str) -> None:
    try:
        f: typing.IO[str] = open(filename, "r")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return
    content: str = f.read()
    f.close()
    print("---")
    print(content, end="")
    print("---")
    print(f"File '{filename}' closed.")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    recover(filename)


if __name__ == "__main__":
    main()
