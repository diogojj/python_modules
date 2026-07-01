"""Alembic 2: 'import ...' to reach alchemy/elements.py."""
import alchemy.elements


def main() -> None:
    """Demonstrate reaching a nested module with a dotted import."""
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print(f"Testing create_earth: {alchemy.elements.create_earth()}")


if __name__ == "__main__":
    main()
