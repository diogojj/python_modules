"""Public surface of the ex0 package.

Note what is *absent*: Flameling, Pyrodon, Aquabub, Torragon. Callers can only
obtain a Creature through a factory, which is exactly the encapsulation the
abstract-factory pattern is meant to provide.
"""

from .creature import Creature
from .factory import AquaFactory, CreatureFactory, FlameFactory

__all__ = ["Creature", "CreatureFactory", "FlameFactory", "AquaFactory"]
