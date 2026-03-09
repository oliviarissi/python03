#!/usr/bin/env python3

import math


def calculate_distance(org: tuple[int, int, int],
                       pos: tuple[int, int, int]) -> None:
    """Print the Euclidean distance between two 3D coordinates.

    Args:
        org: Origin coordinate (x, y, z).
        pos: Target coordinate (x, y, z).
    """

    dist = math.sqrt((pos[0]-org[0])**2 + (pos[1]-org[1])**2 +
                     (pos[2]-org[2])**2)

    print(f"Distance between {org} and {pos}: {dist:.2f}\n")


def parse_coordinates(coor_str: str) -> tuple[int, int, int]:
    """Parse a comma-separated string into a 3D coordinate tuple.

    Args:
        coor_str: Coordinate string in the format "x,y,z".

    Returns:
        tuple: Parsed (x, y, z) integers, or None if conversion fails.

    Raises:
        ValueError: If the input does not contain exactly three values.
    """

    parts = coor_str.split(sep=",")

    if len(parts) != 3:
        raise ValueError("Error parsing coordinates: " +
                         "Coordinates must have 3 values\n")

    try:
        x, y, z = int(parts[0]), int(parts[1]), int(parts[2])
        return (x, y, z)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: (\"{e}\")\n")
        return None


def main() -> None:
    """Run the Game Coordinate System demo.

    Demonstrates coordinate creation, parsing from strings,
    distance calculation, and tuple unpacking.
    """

    print("=== Game Coordinate System ===\n")

    origin = (0, 0, 0)

    pos1 = (10, 20, 5)
    print(f"Position created: {pos1}")
    calculate_distance(origin, pos1)

    print("Parsing coordinates: \"3,4,0\"")
    pos2 = parse_coordinates("3,4,0")
    if pos2:
        print(f"Parsed position: {pos2}")
        calculate_distance(origin, pos2)

    print("Parsing invalid coordinates: \"abc,def,ghi\"")
    pos3 = parse_coordinates("abc,def,ghi")
    if pos3:
        print(f"Position created: {pos3}")
        calculate_distance(origin, pos3)

    if pos2:
        x, y, z = pos2
        print("Unpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
