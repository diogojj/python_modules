class GardenError(Exception):
    """Base error for anything that can go wrong in the garden."""

    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Raised when a plant runs into trouble."""

    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    """Water a plant; reject names that are not capitalised."""
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants: list[str]) -> None:
    """Water a batch of plants, always closing the system afterwards."""
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    test_watering_system(["Spinach", "Pepper", "Basil"])
    print()
    print("Testing invalid plants...")
    test_watering_system(["Spinach", "pepper", "Basil"])
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
