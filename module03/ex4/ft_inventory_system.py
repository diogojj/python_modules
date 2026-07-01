import sys


def main() -> None:
    """Parse 'name:qty' parameters into a dict and analyse the inventory."""
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for param in sys.argv[1:]:
        parts: list[str] = param.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{param}'")
            continue
        name: str = parts[0]
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            quantity: int = int(parts[1])
        except ValueError as err:
            print(f"Quantity error for '{name}': {err}")
            continue
        inventory.update({name: quantity})

    if len(inventory) == 0:
        print("Empty inventory. Usage: python3 ft_inventory_system.py "
              "<item>:<qty> ...")
        return

    print(f"Got inventory: {inventory}")
    items: list[str] = list(inventory.keys())
    print(f"Item list: {items}")
    total: int = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")
    for name in inventory:
        percent: float = round(inventory[name] / total * 100, 1)
        print(f"Item {name} represents {percent}%")

    most: str = items[0]
    least: str = items[0]
    for name in inventory:
        if inventory[name] > inventory[most]:
            most = name
        if inventory[name] < inventory[least]:
            least = name
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({"mana_crystal": 4})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
