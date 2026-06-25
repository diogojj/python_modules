"""Alembic 4: 'import alchemy' only exposes the package public interface."""
import alchemy


def main() -> None:
    """Show that a name absent from __init__ cannot be reached."""
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth: ", end="")
    # create_earth is not re-exported in alchemy/__init__.py:
    # mypy error + AttributeError raised here on purpose.
    print(f"{alchemy.create_earth()}")


if __name__ == "__main__":
    main()
