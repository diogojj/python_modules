import sys
import typing


def read_archive(filename: str) -> str | None:
    try:
        f: typing.IO[str] = open(filename, "r")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return None
    content: str = f.read()
    f.close()
    print("---")
    print(content, end="")
    print("---")
    print(f"File '{filename}' closed.")
    return content


def transform(content: str) -> str:
    new_lines: list[str] = []
    for line in content.splitlines():
        new_lines.append(line + "#")
    return "\n".join(new_lines) + "\n"


def save_archive(content: str) -> None:
    name: str = input("Enter new file name (or empty): ")
    if not name:
        print("Not saving data.")
        return
    print(f"Saving data to '{name}'")
    try:
        f: typing.IO[str] = open(name, "w")
    except OSError as e:
        print(f"Error opening file '{name}': {e}")
        return
    f.write(content)
    f.close()
    print(f"Data saved in file '{name}'.")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    content: str | None = read_archive(filename)
    if content is None:
        return
    new_content: str = transform(content)
    print("Transform data:")
    print("---")
    print(new_content, end="")
    print("---")
    save_archive(new_content)


if __name__ == "__main__":
    main()
