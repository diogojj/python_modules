"""Potions: combine elements coming from near and distant files."""
from .elements import create_earth, create_air  # relative: same package
import elements  # absolute: the distant root-level module


def healing_potion() -> str:
    """Brew a healing potion from earth and air (in-package elements)."""
    earth = create_earth()
    air = create_air()
    return f"Healing potion brewed with '{earth}' and '{air}'"


def strength_potion() -> str:
    """Brew a strength potion from fire and water (root elements)."""
    fire = elements.create_fire()
    water = elements.create_water()
    return f"Strength potion brewed with '{fire}' and '{water}'"
