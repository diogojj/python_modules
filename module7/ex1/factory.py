"""Family factories for the capability-bearing creatures.

They reuse the abstract factory defined in ex0 (CreatureFactory), proving the
ex0 contract is general enough to extend without modification.
"""

from ex0.creature import Creature
from ex0.factory import CreatureFactory

from .creature import Bloomelle, Morphagon, Shiftling, Sproutling


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
