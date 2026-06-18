class GardenError(Exception):
    """Base error for anything that can go wrong in the garden."""

    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Raised when a plant runs into trouble."""

    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Raised when the watering system runs into trouble."""

    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant() -> None:
    """Report a struggling plant by raising a PlantError."""
    raise PlantError("The tomato plant is wilting!")


def check_water_tank() -> None:
    """Report an empty tank by raising a WaterError."""
    raise WaterError("The irrigation tank ran dry!")


def test_custom_errors() -> None:
    """Catch each specific error, then catch them all as GardenError."""
    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print()
    print("Testing WaterError...")
    try:
        check_water_tank()
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print()
    print("Testing catching all garden errors...")
    for failing in (check_plant, check_water_tank):
        try:
            failing()
        except GardenError as error:
            print(f"Caught GardenError: {error}")

    print()
    print("All custom error types work correctly!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    test_custom_errors()


if __name__ == "__main__":
    main()
