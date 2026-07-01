"""Alembic 0: 'import ...' to reach the local elements.py file."""
import elements


def main() -> None:
    """Demonstrate the plain ``import module`` structure."""
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    print(f"Testing create_fire: {elements.create_fire()}")


if __name__ == "__main__":
    main()
