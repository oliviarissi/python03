#!/usr/bin/env python3

import sys

def function() -> None:
    pass


def main() -> None:
    
    print("=== Inventory System Analysis ===")

    inventory = {}
    try:
        for item in sys.argv[1:]:
            name, qty = item.split(":")
            qty = int(qty)
            current = inventory.get(name, 0)
            inventory.update({name:qty+current})

    except ValueError:
        print(f"Error with {name}: {qty} is not valid int. Skipping this input")

    total_items = 0
    for value in inventory.values():
        total_items += value
    
    print(f"Total items in inventory: {total_items}")

    item_types = len(inventory)
    
    print(f"Unique item types: {item_types}\n")
    
    print("=== Current Inventory ===")
    for name, qtu in inventory.items():
        print(f"{name}: {qty} units")
    print(inventory)

        


if __name__ == "__main__":
    main()
