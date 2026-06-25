"""The Abstract Factory layer for exercise 0.

A factory knows how to build a *whole family* of related creatures (a base form
and its evolved form) without the caller ever naming a concrete class.
"""

from abc import ABC, abstractmethod

from .creature import Aquabub, Creature, Flameling, Pyrodon, Torragon


class CreatureFactory(ABC):
    """Abstract factory: the interface every family factory must respect."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Build the base (un-evolved) creature of the family."""
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Build the evolved creature of the family."""
        ...


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
