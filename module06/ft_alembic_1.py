"""Alembic 1: 'from ... import ...' to reach the local elements.py file."""
from elements import create_water


def main() -> None:
    """Demonstrate the ``from module import name`` structure."""
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to access elements.py")
    print(f"Testing create_water: {create_water()}")


if __name__ == "__main__":
    main()
