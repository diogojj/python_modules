"""Capability interfaces.

Key design choice required by the subject: these abstractions do NOT inherit
from Creature. A capability is an orthogonal trait that could one day be glued
onto something other than a creature, so it stays independent.
"""

from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Something that can heal."""

    @abstractmethod
    def heal(self) -> str:
        """Return a message describing the heal action."""
        ...


class TransformCapability(ABC):
    """Something that can transform and revert, with persistent state.

    The `transformed` flag is read by the owner's attack(), so transforming
    actually changes how the entity behaves.
    """

    def __init__(self) -> None:
        self.transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        """Enter the transformed state and return a message."""
        ...

    @abstractmethod
    def revert(self) -> str:
        """Leave the transformed state and return a message."""
        ...
