#!/usr/bin/env python3

import sys


def main() -> None:
    """Run the Inventory System Analysis CLI.

    Parses command-line item:quantity pairs, computes totals,
    displays current inventory, statistics, item categories, and
    restocking suggestions.

    Raises:
        ValueError: If a quantity cannot be converted to an integer
            (caught and reported for each invalid input).
    """

    print("=== Inventory System Analysis ===")

    inventory = {}
    try:
        for item in sys.argv[1:]:
            name, qty = item.split(":")
            qty = int(qty)
            current = inventory.get(name, 0)
            inventory.update({name: qty+current})

    except ValueError:
        print(f"Error with {name}: {qty} is not an int. Skipping this input")

    total_items = 0
    for value in inventory.values():
        total_items += value
    item_types = len(inventory)

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {item_types}")
    print()

    if total_items == 0:
        print("No items in inventory, exiting program")
        return

    print("=== Current Inventory ===")
    for name, qty in sorted(inventory.items(),
                            key=lambda x: x[1], reverse=True):
        qty_percent = (qty / total_items) * 100
        unit = "unit" if qty == 1 else "units"
        print(f"{name}: {qty} {unit} ({qty_percent:.1f}%)")
    print()

    print("=== Inventory Statistics ===")
    min_item, min_qty = min(inventory.items(), key=lambda x: x[1])
    max_item, max_qty = max(inventory.items(), key=lambda x: x[1])
    min_unit = "unit" if min_qty == 1 else "units"
    max_unit = "unit" if max_qty == 1 else "units"
    print(f"Most abundant: {max_item} ({max_qty} {max_unit})")
    print(f"Least abundant: {min_item} ({min_qty} {min_unit})")
    print()

    print("=== Item Categories ===")
    moderate = {}
    scarce = {}
    for name, qty in inventory.items():
        if qty > 4:
            moderate.update({name: qty})
        else:
            scarce.update({name: qty})
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")
    print()

    print("=== Management Suggestions ===")
    restock = {}
    for name, qty in inventory.items():
        if qty <= 1:
            restock.update({name: qty})
    print(f"Restock needed: {", ".join(restock.keys())}")
    print()

    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {", ".join(inventory.keys())}")
    values = [str(value) for value in inventory.values()]
    print(f"Dictionary values: {", ".join(values)}")
    print(f"Sample lookup- 'sword' in inventory: {"sword" in inventory}")


if __name__ == "__main__":
    main()
