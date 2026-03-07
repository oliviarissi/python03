#!/usr/bin/env python3


def main() -> None:

    print("=== Achievement Tracker System ===\n")

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
               'speed_demon', 'perfectionist'}

    print("=== Achievement Tracker System ===")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===")
    all_unique = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}\n")

    common = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common}")

    shared = (
        alice.intersection(bob)
        .union(alice.intersection(charlie))
        .union(bob.intersection(charlie))
        )
    distinct = all_unique - shared
    print(f"Rare achievements (1 player): {distinct}\n")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
