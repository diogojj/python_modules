"""Public surface of ex1: the capability interfaces and the factories.

Concrete creatures stay hidden, just like in ex0.
"""

from .capability import HealCapability, TransformCapability
from .factory import HealingCreatureFactory, TransformCreatureFactory

__all__ = [
    "HealCapability",
    "TransformCapability",
    "HealingCreatureFactory",
    "TransformCreatureFactory",
]
