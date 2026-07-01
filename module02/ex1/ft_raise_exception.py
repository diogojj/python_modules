def input_temperature(temp_str: str) -> int:
    """Convert a reading and reject values outside the safe plant range."""
    temperature = int(temp_str)
    if temperature > 40:
        raise ValueError(
            f"{temperature}°C is too hot for plants (max 40°C)"
        )
    if temperature < 0:
        raise ValueError(
            f"{temperature}°C is too cold for plants (min 0°C)"
        )
    return temperature


def test_temperature() -> None:
    """Check normal, malformed, and out-of-range sensor values."""
    readings: list[str] = ["30", "frost", "55", "-12"]
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
    print("=== Greenhouse Temperature Checker ===")
    print()
    test_temperature()


if __name__ == "__main__":
    main()
