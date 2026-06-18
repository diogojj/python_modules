import math


def get_player_pos() -> tuple[float, float, float]:
    """Prompt the user until a valid 'x,y,z' triple of floats is given."""
    prompt: str = "Enter new coordinates as floats in format 'x,y,z': "
    while True:
        try:
            raw: str = input(prompt)
        except EOFError:
            print("Invalid syntax")
            raise SystemExit(1)
        parts: list[str] = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        coords: list[float] = []
        failed: bool = False
        for part in parts:
            try:
                coords.append(float(part))
            except ValueError as err:
                print(f"Error on parameter '{part.strip()}': {err}")
                failed = True
                break
        if failed:
            continue
        return (coords[0], coords[1], coords[2])


def main() -> None:
    """Read two 3D points and report distances using tuples."""
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    to_center: float = math.sqrt(
        first[0] ** 2 + first[1] ** 2 + first[2] ** 2
    )
    print(f"Distance to center: {round(to_center, 4)}")
    print("Get a second set of coordinates")
    second: tuple[float, float, float] = get_player_pos()
    between: float = math.sqrt(
        (second[0] - first[0]) ** 2
        + (second[1] - first[1]) ** 2
        + (second[2] - first[2]) ** 2
    )
    print(f"Distance between the 2 sets of coordinates: {round(between, 4)}")


if __name__ == "__main__":
    main()
