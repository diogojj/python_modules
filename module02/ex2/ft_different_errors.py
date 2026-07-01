def garden_operations(operation_number: int) -> None:
    """Run a piece of code that fails differently per operation number."""
    if operation_number == 0:
        print(int("seventeen"))
    elif operation_number == 1:
        print(120 / 0)
    elif operation_number == 2:
        handle = open("/var/sensors/ghost_probe.log")
        handle.close()
    elif operation_number == 3:
        print("soil moisture: " + 42)  # type: ignore[operator]
    else:
        return


def test_error_types() -> None:
    """Trigger each error, catch it, and prove the program survives."""
    for number in range(5):
        print(f"Testing operation {number}...")
        try:
            garden_operations(number)
            if number >= 4:
                print("Operation completed successfully")
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")

    print()
    print("Now catching several types with one try block...")
    for number in (0, 1):
        try:
            garden_operations(number)
        except (ValueError, ZeroDivisionError) as error:
            print(f"Caught a data problem: {error}")

    print()
    print("All error types tested successfully!")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()


if __name__ == "__main__":
    main()
