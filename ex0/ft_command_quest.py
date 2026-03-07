#!/usr/bin/env python3

import sys


def main() -> None:

    argc = len(sys.argv)

    print("=== Command Quest ===")

    if argc == 1:
        print("No arguments provided!")

    print(f"Program name: {sys.argv[0]}")

    if argc != 1:
        print(f"Arguments received: {argc - 1}")
        for i in range(1, argc):
            print(f"Argument {i}: {sys.argv[i]}")

    print(f"Total arguments: {argc}\n")


if __name__ == "__main__":
    main()
