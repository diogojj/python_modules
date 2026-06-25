"""Alembic 5: 'from alchemy import ...' pulls a name from the package."""
from alchemy import create_air


def main() -> None:
    """Demonstrate ``from package import name``."""
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
