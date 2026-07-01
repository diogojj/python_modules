"""Test script for the ex1 package (run from the repository root)."""

from ex0 import Creature
from ex1 import (
    HealCapability,
    HealingCreatureFactory,
    TransformCapability,
    TransformCreatureFactory,
)


def test_healing(creature: Creature) -> None:
    """Describe, attack, then heal. Assumes a healing creature."""
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, HealCapability):
        print(creature.heal())


def test_transform(creature: Creature) -> None:
    """Describe, attack, transform, attack again, revert."""
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, TransformCapability):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


def main() -> None:
    print("Testing Creature with healing capability")
    healing = HealingCreatureFactory()
    print(" base:")
    test_healing(healing.create_base())
    print(" evolved:")
    test_healing(healing.create_evolved())

    print()
    print("Testing Creature with transform capability")
    transforming = TransformCreatureFactory()
    print(" base:")
    test_transform(transforming.create_base())
    print(" evolved:")
    test_transform(transforming.create_evolved())


if __name__ == "__main__":
    main()
