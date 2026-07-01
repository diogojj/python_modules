"""Abstract Strategy pattern.

A strategy encapsulates *how* a creature behaves in a fight. The tournament
code stays completely ignorant of capabilities: it just calls strategy.act().
Adding a new behaviour later means adding a new strategy class, nothing else.
"""

from abc import ABC, abstractmethod

from ex0 import Creature
from ex1 import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """Raised when a strategy is applied to an unsuitable creature."""


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Return True if this strategy can be applied to `creature`."""
        ...

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Run the creature's turn. Raises if the combination is invalid."""
        ...


class NormalStrategy(BattleStrategy):
    """Works for any creature: just attack."""

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    """Only for creatures that can transform: transform, attack, revert."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    """Only for creatures that can heal: attack, then heal."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, HealCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())
