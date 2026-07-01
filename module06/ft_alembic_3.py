"""Alembic 3: 'from ... import ...' to reach alchemy/elements.py."""
from alchemy.elements import create_air


def main() -> None:
    """Demonstrate importing a single name from a nested module."""
    print("=== Alembic 3 ===")
    print(
        "Accessing alchemy/elements.py using "
        "'from ... import ...' structure"
    )
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
