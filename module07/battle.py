"""Test script for the ex0 package (run from the repository root)."""

from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    """Verify a factory builds a base and an evolved creature that work.

    Works on *any* CreatureFactory: it never references a concrete class.
    """
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(first: CreatureFactory, second: CreatureFactory) -> None:
    """Make the base creatures of two families fight."""
    print("Testing battle")
    a = first.create_base()
    b = second.create_base()
    print(a.describe())
    print(" vs.")
    print(b.describe())
    print(" fight!")
    print(a.attack())
    print(b.attack())


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()

    test_factory(flame)
    print()
    test_factory(aqua)
    print()
    test_battle(flame, aqua)


if __name__ == "__main__":
    main()
