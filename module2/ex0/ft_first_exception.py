def input_temperature(temp_str: str) -> int:
    """Convert a raw sensor string into an integer temperature."""
    return int(temp_str)


def test_temperature() -> None:
    """Feed valid and corrupted readings into input_temperature()."""
    readings: list[str] = ["18", "frost"]
    for raw in readings:
        print(f"Input data is '{raw}'")
        try:
            temperature = input_temperature(raw)
            print(f"Temperature is now {temperature}°C")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")
        print()
    print("All tests completed - program didn't crash!")


def main() -> None:
    print("=== Greenhouse Sensor Intake ===")
    print()
    test_temperature()


if __name__ == "__main__":
    main()
